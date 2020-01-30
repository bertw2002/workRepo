var fibonacci = function(n) {
  if (n == 0) return 0;
  if (n == 1) return 1;
  return fibonacci(n - 1) + fibonacci(n - 2);
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
