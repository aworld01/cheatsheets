/*
The toPrecision() metnod formats a number to a specified length.
A decimal point and nulls are added (if needed), to create the specified length.
Syntax:-
    variableName.toPrecision(y);
Where y is the number of digits. If omitted, it returns the entire number (without any formatting)
*/

var a = 19.65823;
var ab = a.toPrecision();
console.log(ab);

var ac = a.toPrecision(2);
console.log(ac);

var ad = a.toPrecision(4);
console.log(ad);

var af = a.toPrecision(9);
console.log(af);