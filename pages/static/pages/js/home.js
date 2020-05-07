let navToggler = document.querySelector('nav .navbar-toggler');
let navCollapser = document.querySelector('.navbar-collapse#navbarSupportedContent');
let idMain = document.querySelector('#main');
let body = document.querySelector('body');

navToggler.onclick = function () {
        

  if (!navCollapser.classList.contains('show')) {
    
    idMain.style.height = '150%';
    body.style.backgroundSize = ' auto 130%'

  } else {
    
    idMain.style.height = '100%';
    body.style.backgroundSize = ' auto 100%'

  }

};



let aboutBtn = document.getElementsByClassName("about-btn")[0];
let venobox = document.getElementsByClassName("venobox")[0];
let closeIcons = document.getElementsByClassName("close");
let aboutModal = document.getElementById('aboutModal');
let videoModal = document.getElementById('videoModal');
let modals = document.getElementsByClassName("modal");

// When the user clicks on the button, open the modal
venobox.addEventListener("click", function() {

  videoModal.style.display = "block"

});
aboutBtn.addEventListener("click", function() {

  aboutModal.style.display = "block"

});



// When the user clicks on <span> (x), close the modal
for (obj of closeIcons) {

  obj.onclick = function () {

    this.parentNode.parentNode.style.display = "none"

  }

};
for (i = 0; i < modals.length; i++) {

  let modal = modals.item(i);
  modal.onclick = function(event) {

    if (event.target == this) {

      this.style.display = 'none';
      if (this.id == 'videoModal') {

        const modalContent = this.querySelector('.modal-content');
        modalContent.querySelector('iframe').remove();
        modalContent.innerHTML = '<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/uTMwEh-zR14" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen class="w-100 h-100">Your browser does not support HTML5 video.</iframe>'

      }

    }

  }
        
}