/*
Number methods list:-
1: toString();
2: toExponential()
3: toFixed()
4: toPrecision()
5: valueOf()
6: isFinite()
7: isInteger()
8: isNaN()
9: isSafeInteger()

toString() method returns a number as a string in other world it converts number into string.
We can use this method to output numbers as hexadecimal(16), octal(8), binary(2).
*/
var a = 10;
console.log(a, typeof(a)); //to check datatype

var b = a.toString(); //to change into string.
console.log(b, typeof(b));

var c = a.toString(2); //to change into binary
console.log(c, typeof(c));

var d = a.toString(8); //to change into binary
console.log(d, typeof(d));

var e = a.toString(16); //to change into hexadecimal
console.log(e, typeof(e));