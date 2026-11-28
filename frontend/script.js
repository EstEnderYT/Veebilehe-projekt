const nupp = document.getElementById("teemaNupp");
const root = document.documentElement;

function onTumeTeema() {
    if (root.classList.contains("dark")) return true;
    if (root.classList.contains("light")) return false;
    return window.matchMedia("(prefers-color-scheme: dark)").matches;
}

function uuendaNupuTekst() {
    if (!nupp) return;
    nupp.textContent = onTumeTeema() ? "☾" : "☀";
}

const salvestatud = localStorage.getItem("teema");
if (salvestatud === "light" || salvestatud === "dark") {
    root.classList.add(salvestatud);
}
uuendaNupuTekst();

if (nupp) {
    nupp.addEventListener("click", () => {
        const uusTeema = onTumeTeema() ? "light" : "dark";
        root.classList.remove("light", "dark");
        root.classList.add(uusTeema);
        localStorage.setItem("teema", uusTeema);
        uuendaNupuTekst();
    });
}