const menuBtn = document.querySelector(".menu-btn");
const exitBtn = document.querySelector(".exit-btn");
const menu = document.querySelector("nav ul");

menuBtn.addEventListener("click", () => {
    menu.style.transform = "translateX(0)";
});

exitBtn.addEventListener('click', () => {
    menu.style.transform = 'translateX(100%)';
});

const scrollReveal = ScrollReveal({
    origin: "top",
    distance: "32px",
    duration: 700,
    reset: true
});

scrollReveal.reveal(
    "main, .gallery"
    , { interval: 100 }
);