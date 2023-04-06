/*
The conditional (ternary) operator is the only javaScript operator that takes three operands.
This is the shorter version of IF, ELSE
example:
    variableName = (condition) ? value1 : value2;
*/

/* example1 (if, else) */
// var age = 19;
// if(age >= 18){
//     console.log("You are eligible to vote");
// }else{
//     console.log("You are not eligible to vote");
// }



/* example2 (ternary operator) */
var age = 18;
age = (age >= 18) ? console.log("You are eligible to vote") : console.log("You are not eligible to vote");