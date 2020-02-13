var c = document.getElementById("slate");
var ctx = c.getContext("2d");
var circle = document.getElementById("go");
var pause = document.getElementById("stop");

var increase = 1;
var rad = 15;
var id = 0;
var starting = false;

var stopfunct = function() {
  window.cancelAnimationFrame(id);
  id = 0;
  increase = 0;
  starting = false;
}

pause.addEventListener('click', stopfunct);

var makecircle = function() {
  if (rad >= 300){
    increase  = -1
  }
  if (rad == 0){
    increase = 1
  }
  rad += increase
  ctx.beginPath();
  ctx.clearRect(0, 0, 600, 600);
  ctx.arc(c.width / 2, c.height / 2, rad, 0, Math.PI*2);
  ctx.stroke();
  ctx.fillStyle = "green";
  ctx.fill();
  if (id != 0) {
    id = window.requestAnimationFrame(makecircle);
  }
};

var eventcircle = function(e){
  if (starting == false){
    id = window.requestAnimationFrame(makecircle);
    makecircle();
    increase = 1;
    starting = true;
  }
};
circle.addEventListener('click', eventcircle);
