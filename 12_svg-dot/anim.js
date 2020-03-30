//Albert wan
//softdev1 pd09
//k12 -- connect the dots
//2020-03-29
var clear = document.getElementById("clear");
var canvas = document.getElementById("canvas");

var lastX = -10000;
var lastY = -10000;
var draw = function() {
  var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
  c.setAttribute("cy", event.offsetY);
  c.setAttribute("cx", event.offsetX);
  c.setAttribute("r", 6);
  c.setAttribute("fill", "black");
  canvas.appendChild(c);
  if (lastX == -10000) lastX = event.offsetX
  if (lastY == -10000) lastY = event.offsetY
  else{
    var l = document.createElementNS('http://www.w3.org/2000/svg','line');
    l.setAttribute("x1", lastX);
    l.setAttribute("y1", lastY);
    l.setAttribute("x2", event.offsetX);
    l.setAttribute("y2", event.offsetY);
    l.setAttribute("stroke", "black");
    canvas.appendChild(l);

    lastX = event.offsetX;
    lastY = event.offsetY;
  }
  canvas.appendChild(c);

}

var clearC = function() {
  lastX = -10000;
  lastY = -10000;
  while(canvas.childElementCount > 0){
    canvas.removeChild(canvas.children[0]);
  }
}
clear.addEventListener("click", clearC);

canvas.addEventListener("click",draw);
