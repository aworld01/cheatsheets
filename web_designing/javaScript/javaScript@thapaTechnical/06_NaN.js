/*
NaN is a property of the global object. (not any datatype)
In other words, it is a variable in global scope.
The initial value of NaN is Not-A-Number
*/
var myName = "Abdul Zoha";
var myPhone = 9006228083;

/* example1 */
// console.log(myName - myPhone); //NaN


/* example2 */
// console.log(isNaN(myName)) //to check NaN
// console.log(isNaN(myPhone));



/* example3 */
// var input = "Hello world...";

// if(isNaN(input)){
//     console.log("You are welcome sir...");
// }else{
//     console.log("Invalid input...");
// };



/* example4 */
console.log(NaN === NaN); //false
console.log(Number.NaN === NaN); //false
console.log(isNaN(NaN)); //true
console.log(isNaN(Number.NaN)); //true
console.log(Number.isNaN(NaN)); //true