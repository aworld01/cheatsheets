/*
It creates object with the date specified by the integer values for the year, month, day, hours, minutes, second, milliseconds.

new Date(year, month, day, hours, minutes, seconds, milliseconds);
ex:
    var tarikh = new Date(2018, 4, 25, 9, 45, 35, 0);

You can omit some of the arguments.
*/

var tarikh1 = new Date(2018, 4, 25, 9, 45, 35, 0);
var tarikh2 = new Date(2018, 4, 25, 9, 45, 35);
var tarikh3 = new Date(2018, 4, 25, 9, 45);
var tarikh4 = new Date(2018, 4, 25, 9);
var tarikh5 = new Date(2018, 4, 25);
var tarikh6 = new Date(2018, 4);
var tarikh7 = new Date(8640000);

console.log(tarikh1);
console.log(tarikh2);
console.log(tarikh3);
console.log(tarikh4);
console.log(tarikh5);
console.log(tarikh6);
console.log(tarikh7);