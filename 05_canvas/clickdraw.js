//Albert Wan
//SoftDev2 pd9
//K04 -- I See a Red Door...
//2020-02-06
var canvas = document.getElementById("slate");
var cleary = document.getElementById("clearrect");
var toggley = document.getElementById("toggle");
var ctx = canvas.getContext("2d");
var which = true
//e.preventDefault(); -> used to cancel the original function to an event.
//can be used for toggling the mode to rectangle or dot.

var whichstate = function(e){
  if (which){
    which = false
  }
}
var addshape = function(e){

  var xcor = e.offsetX;
  //gives coordinate of mouse at x coordinate.
  var ycor = e.offsetY;
  //gives coordinate of mouse at Y coordinate.
  if (which){
    ctx.fillStyle = 'blue';
    ctx.fillRect(xcor, ycor , 100, 50);
  }else{
    ctx.beginPath();
    //begins new path, deleting old paths. You do the function every time you want
    //draw a new thing
    console.log("ellipse");
    ctx.fillStyle = 'green';
    ctx.beginPath();
    ctx.ellipse(xcor, ycor , 15,0, Math.PI*2);
    ctx.fill();
  }
}
var clearrect = function(e){
  ctx.clearRect(0, 0, canvas.width, canvas.height);
}

cleary.addEventListener('click', clearrect);
toggley.addEventListener('click', whichstate);
canvas.addEventListener('click', addshape);
