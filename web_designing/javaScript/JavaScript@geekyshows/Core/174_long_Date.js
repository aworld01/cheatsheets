/*
Long dates are most often written with a "MMM DD YYYY" format.
Month and Day can be in any order.
Month can be written in fulll (January), or abbrevated (Jan).
If you write "June, 21, 2018" commans are ignored and names are case insensitive.
*/

/* example-1 */
var tarikh1 = new Date("Mar 25 2018");
var tarikh2 = new Date("March 25 2018");
console.log(tarikh1);
console.log(tarikh2);