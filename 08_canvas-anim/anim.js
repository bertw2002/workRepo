var logo = new Image();
logo.src = "logo_dvd.jpg";
var c = document.getElementById("slate");
var ctx = c.getContext("2d");

var xDVD = 30;
var yDVD = 30;
var xIncrem = 1;
var yIncrem = 1;
var circle = document.getElementById("go");
var pause = document.getElementById("stop");
var dvd = document.getElementById("movie");
var increase = 1;
var rad = 15;
var movieID = 0;
var animID = 0;
var starting = false;

var stopfunct = function() {
  window.cancelAnimationFrame(animID);
  window.cancelAnimationFrame(movieID)
  animID = 0;
  movieID = 0;
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

var makedvdMove = function(e){
  ctx.clearRect(0,0,600,600);
  if (yDVD <= 10 || yDVD >= 550){
    yIncrem = yIncrem * -1;
  }
  if (xDVD <= 10 || xDVD >= 550){
    xIncrem = xIncrem * -1;
  }
  xDVD = xDVD + xIncrem;
  yDVD = yDVD + yIncrem;
  ctx.drawImage(logo, xDVD, yDVD);
  if (movieID != 0){
    window.requestAnimationFrame(makedvdMove);
  }
}

var moviefunct = function(e){
  window.cancelAnimationFrame(animID);
  animID = 0;
  if (movieID == 0){
    movieID = window.requestAnimationFrame(makedvdMove);
    xIncrem = 1;
    yIncrem = 1;
  }
}
movie.addEventListener('click', moviefunct);
