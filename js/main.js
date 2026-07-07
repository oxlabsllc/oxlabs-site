// OX Labs — main.js
// Mobile nav, header rule on scroll, active nav link.

(function () {
  "use strict";

  // ----- Header: bottom rule appears once the page scrolls -----
  var header = document.getElementById("site-header");

  function onScroll() {
    header.classList.toggle("scrolled", window.scrollY > 8);
  }

  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // ----- Mobile nav toggle -----
  var navToggle = document.getElementById("nav-toggle");
  var nav = document.getElementById("site-nav");

  navToggle.addEventListener("click", function () {
    var open = nav.classList.toggle("open");
    navToggle.setAttribute("aria-expanded", String(open));
  });

  // Close the menu when a link inside it is clicked
  nav.addEventListener("click", function (e) {
    if (e.target.closest("a")) {
      nav.classList.remove("open");
      navToggle.setAttribute("aria-expanded", "false");
    }
  });

  // ----- Active nav link while scrolling -----
  var sections = ["problem", "how", "who", "why"]
    .map(function (id) {
      return document.getElementById(id);
    })
    .filter(Boolean);

  var navLinks = document.querySelectorAll(".nav-link");

  function setActiveLink() {
    var fromTop = window.scrollY + window.innerHeight * 0.35;
    var currentId = "";

    sections.forEach(function (section) {
      if (section.offsetTop <= fromTop) {
        currentId = section.id;
      }
    });

    navLinks.forEach(function (link) {
      link.classList.toggle("active", link.getAttribute("href") === "#" + currentId);
    });
  }

  window.addEventListener("scroll", setActiveLink, { passive: true });
  setActiveLink();

  // ----- Footer year -----
  document.getElementById("year").textContent = String(new Date().getFullYear());
})();
