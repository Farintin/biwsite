var vids = document.querySelectorAll('.my-row .my-column img');
var vid1 = vids[0];
var vid2 = vids[1];
var vidsCon = document.querySelectorAll('.my-row .my-column');
var vidsCon1 = vidsCon[0];
var vidsCon2 = vidsCon[1];

var vidIf = document.querySelector('#video-con iframe');

vid1.onclick = function() {
  vidIf.getAttributeNode('src').value = 'https://www.youtube-nocookie.com/embed/g3Tb7An8Ggw';
  vidsCon1.style.border = '4px solid #38b0f7';
  vidsCon2.style.border = '0';

  vid1.className = 'cursor';
  vid2.className = 'demo cursor';
}


vid2.onclick = function() {
  vidIf.getAttributeNode('src').value = 'https://www.youtube-nocookie.com/embed/uTMwEh-zR14';
  vidsCon2.style.border = '4px solid #38b0f7';
  vidsCon1.style.border = '0';

  vid2.className = 'cursor';
  vid1.className = 'demo cursor';
}