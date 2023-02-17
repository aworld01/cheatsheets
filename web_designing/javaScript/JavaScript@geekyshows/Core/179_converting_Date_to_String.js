/*
If you want to crate a string in a standard format, Date provides three methods:-
toString();
toUTCString();
toGMTString();

toUTCString() and toGMTString() format the string according to Internet (GMT) standards, whereas toString() creates the string according to Local Time.
*/
var tarikh = new Date();
var d1 = tarikh.toString();
var d2 = tarikh.toUTCString();
var d3 = tarikh.toGMTString();

console.log(d1);
console.log(d2);
console.log(d3);
