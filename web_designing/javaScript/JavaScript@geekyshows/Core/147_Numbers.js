/*
Number type in javaScript includes both integer and floating point values.
javaScrip numbers are always stored as double precision floating point numbers, following the international IEEE 754 standard.
javaScript also provide an object representation of numbers.
ex:-
    12
    23.45
    5e3 / 5x10x10x10 = 5000
    234e-5 = 0.00234


Primitive (type = Number)
-------------------------
var a = 10; // Whole Number
var a = 10.45; // Decimal Number
var a = 5e3; // 5000//5x10^3 exponent
var a = 34e-5; // 0.00034 exponent

Constructor (type = Object)
---------------------------
var a = new Number(10);
var a = new Number(10.45);
var a = new Number(5e3);
*/

var a = 10;
var b = 10.45;
var c = 5e3;
var d = 34e-5;
var e = "500";
var x = new Number(100);
var y = new Number("200");
var z = new Number("400");

console.log(a, typeof(a));
console.log(b, typeof(b));
console.log(c, typeof(c));
console.log(d, typeof(d));
console.log(e, typeof(e));
console.log(x, typeof(x));
console.log(y, typeof(y));
console.log(z, typeof(z));