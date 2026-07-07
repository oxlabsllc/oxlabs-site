// OX Labs — main.js
// Mobile nav, header rule on scroll, active nav link, contact form.

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
  var sections = ["problem", "how", "who", "why", "contact"]
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

  // ----- Contact form (Formspree via fetch, falls back to plain POST without JS) -----
  var form = document.getElementById("contact-form");
  var status = document.getElementById("form-status");
  var submitBtn = document.getElementById("form-submit");

  form.addEventListener("submit", function (e) {
    e.preventDefault();

    status.textContent = "";
    status.className = "form-status";
    submitBtn.disabled = true;
    submitBtn.textContent = "Sending…";

    fetch(form.action, {
      method: "POST",
      body: new FormData(form),
      headers: { Accept: "application/json" },
    })
      .then(function (res) {
        if (res.ok) {
          form.reset();
          status.classList.add("ok");
          status.textContent = "Got it — we'll be in touch within one business day.";
        } else {
          showError();
        }
      })
      .catch(showError)
      .finally(function () {
        submitBtn.disabled = false;
        submitBtn.textContent = "Send Message";
      });
  });

  function showError() {
    status.classList.add("error");
    status.innerHTML =
      'Something went wrong. Email us directly at <a href="mailto:al@oxlabs.com">al@oxlabs.com</a>.';
  }

  // ----- Footer year -----
  document.getElementById("year").textContent = String(new Date().getFullYear());
})();
