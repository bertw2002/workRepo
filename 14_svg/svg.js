//Albert wan
//softdev1 pd09
//k13 -- Ask Circles
//2020-03-31
var xIncrem = 1;
var yIncrem = 1;
var clear = document.getElementById("clear");
var canvas = document.getElementById("canvas");
var xtra = document.getElementById("xtra");
var mo
var draw = function() {

    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    c.setAttribute("cy", event.offsetY);
    c.setAttribute("cx", event.offsetX);
    c.setAttribute("r", 15);
    c.setAttribute("fill", "black");
    c.addEventListener("click", draw1);
    canvas.appendChild(c);


}

var circleMove = function(e) {
  var allCircles = canvas.children;
  var length = allCircles.length;
  for (var x = 0; x < length; x++){
    if (Math.floor(Math.random() * 2) = 0){
      xIncrem = 1;
    }else{
      xIncrem = -1;
    }
    if (Math.floor(Math.random() * 2) = 0){
      yIncrem = 1;
    }else{
      yIncrem = -1;
    }
    var xCor =  allCircles[x].getAttribute("cx") + xIncrem;
    var yCor =  allCircles[x].getAttribute("yx") + yIncrem;
    allCircles[x].setAttribute()
  }

  if (yCor <= 10 || yCor >= 570){
    yIncrem = yIncrem * -1;
  }
  if (xCor <= 10 || xCor >= 570){
    xIncrem = xIncrem * -1;
  }
  circles[i].setAttribute("cy", y);
  circles[i].setAttribute("cx", x);

}

var clearC = function() {
  while(canvas.childElementCount > 0){
    canvas.removeChild(canvas.children[0]);
  }
}
clear.addEventListener("click", clearC);

canvas.addEventListener("click",draw);
