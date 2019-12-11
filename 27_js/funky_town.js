var fibonacci = function(n) {
  if (num == 0) return 0;
  if (num == 1) return 1;
  return fibonacci(num - 1) + fibonacci(num - 2);
};

var gcd = function(a, b) {
  if (a % b == 0){
    return b;
  }
  if (b > a){
    return gcd(b, a);
  }
  return gcd(a - b, b);
};

var randlist = ["topher", "Albert", "Kazi", "Nahi"]
var randomStudent = function(){
  x = Math.random();
  listlength = randlist.length;
  return randlist[Math.floor(listlength * x)];
};
