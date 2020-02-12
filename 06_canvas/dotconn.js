/*
Albert Wan
SoftDev pd9
K06: Dot Dot Dot
2020/2/11
*/
var cleary = document.getElementById("clear");
var canvas = document.getElementById("slate");
var ctx = canvas.getContext("2d");


var clear = function(e){
  ctx.beginPath();
  ctx.clearRect(0, 0, canvas.width, canvas.height);
}

var makedot = function(e){
  var xcor = e.offsetX;
  var ycor = e.offsetY;
  ctx.fillStyle = 'blue';
  ctx.ellipse(xcor, ycor, 3, 3, 0, 0, Math.PI*2);
  ctx.fill();
  ctx.moveTo(xcor, ycor);
  ctx.stroke();
}
cleary.addEventListener('click', clear);
canvas.addEventListener('click', makedot);
