var cleary = document.getElementById("clear");
var ctx = canvas.getContext("2d");
var canvas = document.getElementById("slate");

var clear = function(e){
  ctx.beginPath();
  ctx.clearRect(0, 0, canvas.width, canvas.height);
}

var makedot = function(e){
  var xcor = e.offsetX;
  var ycor = e.offsetY;
  ctx.fillStyle = 'blue';
  ctx.ellipse(xcor, ycor, 5, 5, 0, 0, Math.PI*2);
  ctx.fill();
  ctx.moveTo(xcor, ycor);
  ctx.stroke();
}
cleary.addEventListener('click', clear);
canvas.addEventListener('click', makedot);
