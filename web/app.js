(() => {
  const content = document.getElementById("app-content");
  const navigation = document.getElementById("app-navigation");
  const refreshButton = document.getElementById("actualizar-vista");
  const version = String(Date.now());
  let modules = [];
  const previews = new Map();

  refreshButton.addEventListener("click", () => {
    const url = new URL(window.location.href);
    url.searchParams.set("v", String(Date.now()));
    window.location.replace(url.toString());
  });

  function renderNavigation(modules) {
    navigation.replaceChildren();
    modules.forEach((module) => {
      const link = document.createElement("a");
      link.href = "#" + module.target;
      link.textContent = module.label;
      navigation.appendChild(link);
    });
  }

  function renderModule(target) {
    const module = modules.find((item) => item.target === target) || modules[0];
    if (!module) {
      content.innerHTML = '<p class="estado-error">Todavía no hay un módulo integrado.</p>';
      return;
    }

    const previewDocument = previews.get(module.id);
    if (!previewDocument) {
      content.innerHTML = '<p class="estado-error">No se pudo preparar este módulo.</p>';
      return;
    }

    content.replaceChildren(...Array.from(previewDocument.body.children).map((node) => node.cloneNode(true)));
    navigation.querySelectorAll("a").forEach((link) => {
      link.setAttribute("aria-current", link.hash === "#" + module.target ? "page" : "false");
    });
  }

  function setVisualMessage(message, type = "estado-exito") {
    const messageElement = document.getElementById("estado-inicio");
    if (!messageElement) return;
    messageElement.className = type;
    messageElement.textContent = message;
    messageElement.hidden = false;
  }

  function enableIndependentPreviewBehavior() {
    content.addEventListener("click", (event) => {
      const button = event.target.closest("[data-action]");
      if (!button) return;

      if (button.dataset.action === "close-window") {
        setVisualMessage(
          "En la aplicación de PC, este botón cierra la ventana. En GitHub Pages se muestra la respuesta visual."
        );
      }
    });
  }

  async function loadIntegration() {
    try {
      const configResponse = await fetch("config/integration.json?v=" + version, {
        cache: "no-store"
      });
      if (!configResponse.ok) throw new Error("No se encontró la configuración de integración.");

      const config = await configResponse.json();
      modules = config.active_modules || [];
      renderNavigation(modules);
      content.replaceChildren();

      for (const module of modules) {
        const previewResponse = await fetch(module.preview + "?v=" + version, {
          cache: "no-store"
        });
        if (!previewResponse.ok) throw new Error("No se pudo cargar " + module.preview + ".");

        const previewHtml = await previewResponse.text();
        previews.set(module.id, new DOMParser().parseFromString(previewHtml, "text/html"));
      }

      renderModule(window.location.hash.slice(1));
      enableIndependentPreviewBehavior();
    } catch (error) {
      console.error(error);
      content.innerHTML = '<p class="estado-error">No se pudo cargar la aplicación integrada.</p>';
    }
  }

  window.addEventListener("hashchange", () => renderModule(window.location.hash.slice(1)));
  loadIntegration();
})();
