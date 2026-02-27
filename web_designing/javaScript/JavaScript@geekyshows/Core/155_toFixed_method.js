/*
The toFixed() method converts a number into a string, keeping a specified number of decimals also it rounds the decimal. If the desired number of decimals are higher than the actual number, nulls are added to create the desired decimal length.
Syntax:-
    a.toFixed(y);
Where y is the number of digits after the decimal point. Default is 0 (no digits after the decimal point).
*/

var a = 19.65823;
console.log(a);

var ab = a.toFixed();
console.log(ab);

var ac = a.toFixed(2);
console.log(ac);

var ad = a.toFixed(4);
console.log(ad);

var af = a.toFixed(8);
console.log(af);