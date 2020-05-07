var navTag = document.getElementsByTagName("nav");
var firstNav = navTag[0];

var bgColor = document.getElementById("bgColor");
var regForms = document.querySelectorAll("form .row input");

bgColor.style.top = firstNav.height + "px";
    