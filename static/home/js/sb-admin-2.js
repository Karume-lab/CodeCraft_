(function ($) {
    "use strict"; // Start of use strict

    // Toggle the side navigation
    // Function to toggle sidebar
    function toggleSidebar() {
        $("body").toggleClass("sidebar-toggled");
        $(".sidebar").toggleClass("toggled");
        if ($(".sidebar").hasClass("toggled")) {
            $('.sidebar .collapse').collapse('hide');
            $("#collapseThemes").removeClass("grey-accordion black-accordion");
            $("#collapseViewProjects").removeClass("grey-accordion black-accordion");
            if ($("#accordionSidebar").hasClass("grey-accordion")) {
                $("#collapseThemes").addClass("grey-accordion");
                $("#collapseViewProjects").addClass("grey-accordion");
            } else if ($("#accordionSidebar").hasClass("black-accordion")) {
                $("#collapseThemes").addClass("black-accordion");
                $("#collapseViewProjects").addClass("black-accordion");
            }
        }
    }

    // Add click event listener to the toggle buttons
    $("#sidebarToggle, #sidebarToggleTop").on('click', function (e) {
        toggleSidebar();

        // Store the sidebar state in localStorage
        const isSidebarToggled = $(".sidebar").hasClass("toggled");
        localStorage.setItem("sidebarToggled", isSidebarToggled);
    });

    // Check the stored sidebar state on page load
    $(document).ready(function () {
        const storedSidebarState = localStorage.getItem("sidebarToggled") === "true";

        if (storedSidebarState) {
            toggleSidebar();
        }
    });
    // Close any open menu accordions when window is resized below 768px
    $(window).resize(function () {
        if ($(window).width() < 768) {
            $('.sidebar .collapse').collapse('hide');
        };

        // Toggle the side navigation when window is resized below 480px
        if ($(window).width() < 480 && !$(".sidebar").hasClass("toggled")) {
            $("body").addClass("sidebar-toggled");
            $(".sidebar").addClass("toggled");
            $('.sidebar .collapse').collapse('hide');
        };
    });

    // Prevent the content wrapper from scrolling when the fixed side navigation hovered over
    $('body.fixed-nav .sidebar').on('mousewheel DOMMouseScroll wheel', function (e) {
        if ($(window).width() > 768) {
            var e0 = e.originalEvent,
                delta = e0.wheelDelta || -e0.detail;
            this.scrollTop += (delta < 0 ? 1 : -1) * 30;
            e.preventDefault();
        }
    });

    // Scroll to top button appear
    $(document).on('scroll', function () {
        var scrollDistance = $(this).scrollTop();
        if (scrollDistance > 100) {
            $('.scroll-to-top').fadeIn();
        } else {
            $('.scroll-to-top').fadeOut();
        }
    });

    // Smooth scrolling using jQuery easing
    $(document).on('click', 'a.scroll-to-top', function (e) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: ($($anchor.attr('href')).offset().top)
        }, 1000, 'easeInOutExpo');
        e.preventDefault();
    });

})(jQuery); // End of use strict
