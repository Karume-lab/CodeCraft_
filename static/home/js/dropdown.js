document.addEventListener("click", function(event) {
    const collapseToggles = document.querySelectorAll(".collapse-toggle");
    collapseToggles.forEach(function(collapseToggle) {
        const collapseTarget = document.querySelector(collapseToggle.getAttribute("data-target"));
        if (!collapseToggle.contains(event.target) && !collapseTarget.contains(event.target)) {
            if (collapseTarget.classList.contains("show")) {
                collapseToggle.click();
            }
        }
    });
});
