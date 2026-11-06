// Telefono ed email non sono scritti nell'HTML: i robot che leggono le pagine non li raccolgono.
// Chi visita il sito li vede con un clic. Se il pulsante ha un oggetto (per esempio «Chiedi per email»
// su un libro), il clic apre direttamente il programma di posta con l'email già compilata.
(function () {
  function decodifica(v) {
    var s = atob(v);
    var b = new Uint8Array(s.length);
    for (var i = 0; i < s.length; i++) b[i] = s.charCodeAt(i);
    return new TextDecoder().decode(b).split("").reverse().join("");
  }
  function indirizzo(btn) {
    var valore = decodifica(btn.dataset.v);
    if (btn.dataset.tipo === "tel") return { valore: valore, href: "tel:+39" + valore.replace(/\D/g, "") };
    var parti = [];
    if (btn.dataset.oggetto) parti.push("subject=" + encodeURIComponent(btn.dataset.oggetto));
    if (btn.dataset.testo) parti.push("body=" + encodeURIComponent(btn.dataset.testo));
    return { valore: valore, href: "mailto:" + valore + (parti.length ? "?" + parti.join("&") : "") };
  }
  function rivela(btn) {
    var d = indirizzo(btn);
    if (btn.dataset.oggetto) {
      // Apre l'email compilata e lascia sotto il pulsante l'indirizzo, per chi non ha un programma di posta
      window.location.href = d.href;
      var nota = btn.parentNode.querySelector(".rivela-nota");
      if (!nota) {
        nota = document.createElement("p");
        nota.className = "rivela-nota";
        btn.insertAdjacentElement("afterend", nota);
      }
      nota.textContent = "Se non si apre la posta, scriva a ";
      var a1 = document.createElement("a");
      a1.href = d.href;
      a1.textContent = d.valore;
      nota.appendChild(a1);
      nota.appendChild(document.createTextNode("."));
      return;
    }
    var a = document.createElement("a");
    a.href = d.href;
    a.textContent = d.valore;
    btn.replaceWith(a);
    a.focus();
  }
  document.addEventListener("click", function (e) {
    var btn = e.target.closest && e.target.closest("button[data-v]");
    if (btn) rivela(btn);
  });
})();
