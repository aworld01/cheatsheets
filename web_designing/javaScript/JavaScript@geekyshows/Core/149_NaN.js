/*
The NaN property represents "Not-a-Number" value. This property indicates that a value is not a legal number. NaN never compare equal to anything, even itself.
The NaN property is the same as the Number.Nan property.
*/
var a = "50";
var b = 10;
var d = "Hello";

var w = a-b; //legal number.
var x = b-a; //legal number.
var y = b/d; //ilegal number.

console.log(w);
console.log(x);
console.log(y);