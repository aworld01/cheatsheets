/*
The toExponential() method converts a number into an exponential notation.
Syntax:-
    variableName.toExponential(y);
Where y is an integer between 0 and 20 representing the number of digits in the notation after the decimal point. If omitted, it is set to as many digits as necessary to represent the value.
*/

var a = 58975.98745;
var ab = a.toExponential();
console.log(ab);

var ac = a.toExponential(2);
console.log(ac);

var ad = a.toExponential(4);
console.log(ad);
