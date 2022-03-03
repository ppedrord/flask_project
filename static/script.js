/* Open and close the menu on mobile mode */

const menuMobile = document.querySelector(".menu-mobile");
const body = document.querySelector("body");

menuMobile.addEventListener("click", () => {
  menuMobile.classList.contains("bi-list")
    ? menuMobile.classList.replace("bi-list", "bi-x")
    : menuMobile.classList.replace("bi-x", "bi-list");
  body.classList.toggle("menu-nav-active");
});

/* Close the menu when click on any item and change the icon to list */

const navItem = document.querySelectorAll(".nav-item");

navItem.forEach((item) => {
  item.addEventListener("click", () => {
    if (body.classList.contains("menu-nav-active")) {
      body.classList.remove("menu-nav-active");
      menuMobile.classList.replace("bi-x", "bi-list");
    }
  });
});

/* Animate all items with 'data-animation' attribute */

const item = document.querySelectorAll("[data-animation]");

const animeScroll = () => {
  const windowTop = window.pageYOffset + window.innerHeight * 0.88 ;

  item.forEach((element) => {
    if (windowTop > element.offsetTop) {
      element.classList.add("animate");
    } else {
      element.classList.remove("animate");
    }
  });
};

animeScroll();

window.addEventListener("scroll", ()=>{
  animeScroll();
})

/* Enable Submit button loading */


const btnSubmit = document.querySelector('#btn-submit')
const btnSubmitLoader = document.querySelector('#btn-submit-loader')

btnSubmit.addEventListener("click", ()=>{
  btnSubmitLoader.style.display = "block";
  btnSubmit.style.display = "none"
})


