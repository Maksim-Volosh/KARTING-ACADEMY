const body = document.querySelector("body");
const blackout = document.querySelector(".blackout");
const navbars = document.querySelector(".navbar__items");
const checkbox = document.querySelector("input[type=\"checkbox\"]");

checkbox.addEventListener("click", function toggleMenu() {
    body.classList.toggle("scroll-no");
    navbars.classList.toggle("navbar_show");
    blackout.classList.toggle("blackout-yes");
})

