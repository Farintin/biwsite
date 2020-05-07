// Typing JS Script
$(function () {

  var typed = new Typed('#typed1', {
    strings: ['LCOME TO '],
    typeSpeed: 100,
    loop: true,
    backDelay: 4000
  });


  var typed2 = new Typed('#typed2', {
    strings: ['INSPIRE'],
    typeSpeed: 100,
    loop: true,
    startDelay: 500,
    backDelay: 4000,
  });


  var typed3 = new Typed('#typed3', {
    strings: ['ILLUMINATE'],
    typeSpeed: 100,
    loop: true,
    startDelay: 500,
    backDelay: 4000,
  });


  var typed4 = new Typed('#typed4', {
    strings: ['CREATE'],
    typeSpeed: 100,
    loop: true,
    startDelay: 500,
    backDelay: 4000,
  });

})


// Cards WOW animation
var cards = document.getElementsByClassName('card');
var t = 0.6;
for (card of cards) {
  t += 0.4
  card.style.animation = "flowInRightLeft " + t + "s ease-out 1"
}