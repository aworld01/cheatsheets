/*
Short dates are written with an "MM/DD/YYYY" format.
In some browsers, months, or days with no leading zeroes may produce an error.
The behavior of "YYYY/MM/DD" is undefined. Some browsers will try to guess the format. Some will return NaN.
The behavior of "DD-MM_YYYY" is also undefined. Some browsers will try to guess the format. Some will return NaN.
*/

var tarikh = new Date("06/25/2018");
console.log(tarikh);