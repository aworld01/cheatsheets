/*
The parseFloat() function parses a string and returns a floating point number. This function determines if the first character in the specified string is a number.
If it is, it parses the string until it reaches the end of the number, and returns the number as a number, not as a string.
Syntax:
    parseFloat(string)

Only the first number in the string is returned!
Leading and trailing spaces are allowed.
If the first character can't be converted to a number, parseFloat() returns NaN.
*/

console.log(parseFloat("10"));
console.log(parseFloat("12.00"));
console.log(parseFloat("15.45"));
console.log(parseFloat("10 20 30"));
console.log(parseFloat(" 90 "));
console.log(parseFloat("10 years"));
console.log(parseFloat("years 10"));
console.log(parseFloat("020"));