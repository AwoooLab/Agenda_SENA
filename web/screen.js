(() => {
  const screen = document.getElementById("screen");
  const version = String(Date.now());
  const assets = {
    login: "assets/login-window.svg",
    agenda: "assets/agenda-window.svg"
  };

  async function showScreen(name) {
    const response = await fetch(`${assets[name]}?v=${version}`, { cache: "no-store" });
    if (!response.ok) throw new Error(`No se pudo cargar ${assets[name]}.`);

    screen.innerHTML = await response.text();
    const svg = screen.querySelector("svg");
    if (!svg) throw new Error("El asset no contiene una imagen SVG válida.");

    const next = screen.querySelector('[data-action="next"]');
    if (next) {
      const goToAgenda = () => {
        window.location.hash = "agenda";
      };
      next.addEventListener("click", goToAgenda);
      next.addEventListener("keydown", (event) => {
        if (event.key === "Enter" || event.key === " ") {
          event.preventDefault();
          goToAgenda();
        }
      });
    }
  }

  async function render() {
    const name = window.location.hash === "#agenda" ? "agenda" : "login";
    try {
      await showScreen(name);
    } catch (error) {
      console.error(error);
      screen.innerHTML = "";
    }
  }

  window.addEventListener("hashchange", render);
  render();
})();
