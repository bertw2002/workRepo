//Albert wan
//softdev1 pd09
//k13 -- Ask Circles
//2020-03-31
var clear = document.getElementById("clear");
var canvas = document.getElementById("canvas");
var candraw = true;
var draw = function() {
  if (candraw){
    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    c.setAttribute("cy", event.offsetY);
    c.setAttribute("cx", event.offsetX);
    c.setAttribute("r", 15);
    c.setAttribute("fill", "black");
    c.addEventListener("click", draw1);
    canvas.appendChild(c);
  }
  candraw = true;

}

var draw1 = function(e) {
  this.setAttribute("fill", "orange");
  this.addEventListener("click", erase);
  e.stopPropagation();
}
var erase = function(e) {
    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    randomY = Math.floor(Math.random()*550);
    randomX = Math.floor(Math.random()*550);
    c.setAttribute("fill", "black");
    c.setAttribute("cy", randomY);
    c.setAttribute("cx", randomX);
    c.setAttribute("r", 15);
    canvas.removeChild(this);
    c.addEventListener("click",draw1);
    canvas.appendChild(c);
    candraw = false;

}

var clearC = function() {
  while(canvas.childElementCount > 0){
    canvas.removeChild(canvas.children[0]);
  }
}
clear.addEventListener("click", clearC);

canvas.addEventListener("click",draw);
