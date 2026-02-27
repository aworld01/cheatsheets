/*
javaScrip global methods can be used on all javaScript data types.
Number()
parseFloat()
parseInt()

The Number() function converts the object argument to a number that represents the object's value.
If the value can't be converted to a legal number, NaN is returned.
If the parameter is a Date object, the Number() function returns the number of milliseconds since midnight January 1, 1970 UTC.
Ex:-
    Number(true);
    Number("100");
    Number(100/"Hello");
*/

var a = true;
var b = false;
var c = 100;
var d = "100";
var e = "Hello";
var f = new Date();

console.log("True:", Number(a));
console.log("False:", Number(b));
console.log("100:", Number(c));
console.log("100: ", Number(d));
console.log("Hello: ", Number(e));
console.log("Date: ", Number(f));