/*
The parseInt() function parses a string and returns an integer.
Syntax:-
    parseInt(string, radix);

The redix parameter is used to specify which numeral system to be used, for example, a radix of 16 (hexadecimal) indicates that the number in the string should be parsed from a hexadecimal number to a decimal number.

If the radix parameter is omitted, javaScript assumes the following:
    If the string begins with "0x", the radix is 16 (hexadecimal)
    If the string begins with any other value, the radix is 10 (decimal)

Only the first number in the string is returned.
Leading and trailing spaces are allowed.
If the first character can't be converted to a number. parseInt() returns NaN.
*/

console.log(parseInt("10"));
console.log(parseInt("12.00"));
console.log(parseInt("15.45"));
console.log(parseInt("10 20 30"));
console.log(parseInt(" 90 "));
console.log(parseInt("10 years"));
console.log(parseInt("years 10"));
console.log(parseInt("020"));
console.log(parseInt("12", 8)); //12 octal = 10 decimal
console.log(parseInt("0x12")); //12 hex = 18 decimal
console.log(parseInt("10", 16)); //10 hex = 16 decimal