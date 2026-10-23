"""Generate a checklist showing which planned project files already exist."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STAGES_DIR = ROOT / "stages"
OUTPUT = ROOT / "docs" / "file_status.md"


def read_stage_files(manifest: Path):
    """Yield repository-relative paths listed with a '- ' marker."""
    for line in manifest.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("- "):
            relative_path = line[2:].strip().strip("`")
            if relative_path:
                yield relative_path


def main() -> None:
    rows = [
        "# File status",
        "",
        "Generated automatically from each `stages/*/files.txt` file.",
        "",
        "Legend: ✅ file exists · ⬜ file pending",
        "",
    ]

    for stage in sorted(STAGES_DIR.iterdir()):
        if not stage.is_dir():
            continue

        manifest = stage / "files.txt"
        if not manifest.exists():
            continue

        rows.extend(
            [
                f"## {stage.name}",
                "",
                "| Status | File |",
                "|---|---|",
            ]
        )

        for relative_path in read_stage_files(manifest):
            exists = (ROOT / relative_path).is_file()
            status = "✅" if exists else "⬜"
            rows.append(f"| {status} | `{relative_path}` |")

        rows.append("")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n".join(rows).rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
