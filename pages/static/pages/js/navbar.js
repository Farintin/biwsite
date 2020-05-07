jQuery(document).ready(function($) {
    "use strict";

    let navbar = $('#navbar');
    let navbarHeight = navbar.outerHeight();

    // Moved down below navigation bar height effect
    $(window).on('scroll', function() {

      if ($(window).scrollTop() > navbarHeight) {
        navbar.addClass('fixed-top');
      } else {
        navbar.removeClass('fixed-top');
      }
   	
    });

});