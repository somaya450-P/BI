(function () {
    "use strict";

    function initReveal() {
        var root = document.querySelector(
            ".o_somaya_home, .o_somaya_about, .o_somaya_contact, .o_somaya_projects_list, .o_somaya_project_detail"
        );
        if (!root) {
            return;
        }

        var targets = root.querySelectorAll(
            "section, .o_somaya_work_card, .o_somaya_project_card_big, .o_somaya_skill_card, .o_somaya_tag_card, .o_somaya_contact_card"
        );

        var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

        if (reduceMotion || !("IntersectionObserver" in window)) {
            targets.forEach(function (el) {
                el.classList.add("o_somaya_revealed");
            });
            return;
        }

        targets.forEach(function (el) {
            el.classList.add("o_somaya_reveal");
        });

        var observer = new IntersectionObserver(
            function (entries) {
                entries.forEach(function (entry) {
                    if (entry.isIntersecting) {
                        entry.target.classList.add("o_somaya_revealed");
                        observer.unobserve(entry.target);
                    }
                });
            },
            { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
        );

        targets.forEach(function (el) {
            observer.observe(el);
        });
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initReveal);
    } else {
        initReveal();
    }
})();
