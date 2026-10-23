"""Configuración compartida de la aplicación."""

from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT_DIR / "data" / "agenda.json"
APP_TITLE = "Agenda SENA"
DATE_FORMAT = "%Y-%m-%d"
TIME_FORMAT = "%H:%M"
