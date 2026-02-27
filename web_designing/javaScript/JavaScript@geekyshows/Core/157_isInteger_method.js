/*
The Number.isInteger() method determines whether a value an integer.
This method returns true if the value is of the type Number, and an integer, Otherwise it returns false.
*/

var a = Number.isInteger(); //false
var b = Number.isInteger(100); //true
var c = Number.isInteger(-100); //true
var d = Number.isInteger(100.45); //false
var e = Number.isInteger(200-100); //true
var f = Number.isInteger(0.1); //false
var g = Number.isInteger("100"); //false

console.log(a);
console.log(b);
console.log(c);
console.log(d);
console.log(e);
console.log(f);
console.log(g);