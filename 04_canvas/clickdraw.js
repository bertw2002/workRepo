//Albert Wan
//SoftDev2 pd9
//K04 -- I See a Red Door...
//2020-02-06
var canvas = document.getElementById("slate");
var cleary = document.getElementById("clearrect");
var toggley = document.getElementById("toggle");
var ctx = canvas.getContext("2d");
var which = true


var whichdraw = function(e){
  if (which){
    which = false
  }
}
var addshape = function(e){
  if (which){
    ctx.fillStyle = 'blue';
    ctx.fillRect(e.layerX, e.layerY, 100, 50);
  }else{
    console.log("ellipse");
    ctx.fillStyle = 'green';
    ctx.beginPath();
    ctx.ellipse(e.layerX, e.layerY, 30,30, 0,0, Math.PI*2);
    ctx.fill();
  }
}
var clearrect = function(e){
  ctx.clearRect(0, 0, canvas.width, canvas.height);
}

cleary.addEventListener('click', clearrect);
toggley.addEventListener('click', whichdraw);
canvas.addEventListener('click', addshape);
