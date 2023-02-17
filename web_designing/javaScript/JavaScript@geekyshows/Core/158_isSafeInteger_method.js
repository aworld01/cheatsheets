/*
The Number.isSafeInteger() method determines whether a value is a safe integer.
A safe integer is an integer that can be exactly all integers from (2^53 -1) to -(2^53 -1).
This method returns true if the value is of the type Number, and a safe integer. Otherwise it returns false.
*/
console.log("No Parameter: ", Number.isSafeInteger()); //false
console.log("100: ", Number.isSafeInteger(100)); //true
console.log("-100: ", Number.isSafeInteger(-100)); //true
console.log("100.45: ", Number.isSafeInteger(100.45)); //false
console.log("200-100: ", Number.isSafeInteger(200-100)); //true
console.log("0.1: ", Number.isSafeInteger(0.1)); //false
console.log("'100': ", Number.isSafeInteger("100")); //false