var a = true; //true
var b = false; //false
var c = ""; //false
var d = Boolean(""); //false
var e = Boolean(); //false
var f = Boolean(0); //false
var g = Boolean(-0); //false
var h = Boolean(NaN); //false (Not a Number)
var i = Boolean(null); //false

console.log(a);
console.log(b);
console.log(c);
console.log(d);
console.log(e);
console.log(f);
console.log(g);
console.log(h);
console.log(i);