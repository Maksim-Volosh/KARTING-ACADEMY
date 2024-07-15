const body = document.querySelector("body");
const blackout = document.querySelector(".blackout");
const navbars = document.querySelector(".navbar__items");
const checkbox = document.querySelector("input[type=\"checkbox\"]");
const hamburger = document.querySelector(".hamburger-lines")

checkbox.addEventListener("click", function toggleMenu() {
    body.classList.toggle("scroll-no");
    navbars.classList.toggle("navbar_show");
    blackout.classList.toggle("blackout-yes");
    hamburger.classList.toggle("hamburger-transform");

})

function closeMenu() {
    body.classList.remove("scroll-no");
    navbars.classList.remove("navbar_show");
    blackout.classList.remove("blackout-yes");
    hamburger.classList.remove("hamburger-transform");
}

blackout.addEventListener("click", closeMenu);
