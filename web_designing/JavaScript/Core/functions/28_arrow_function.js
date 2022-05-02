/*
An arrow function expression (previously, and now incorrectly known as fat arrow function) has a shorter syntax compared to function expressions. Arrow functions are always anonymous.

You can't call arrow function before define.
*/

// // function expression
// var myfun1 = function show(){
//     console.log("This is a function expression...");
// };
// myfun1();


//  // anonymous function
//  var myfun2 = function(){
//     console.log("This is an anonymous function...");
// };
// myfun2();


// // arrow function
// var myfun3 = () =>{
//     console.log("This is an arrow function...");
// };
// myfun3()





// // arrow_function with parameter
// var myfun3 = (a) => {
//     console.log(a);
// };
// myfun3(20)


// // arrow_function with default parameter
// var myfun3 = (a,b=20) => {
//     console.log(a, b);
// };
// myfun3(30)


// // arrow_function with rest parameter
// var myfun3 = (a,...args) => {
//     console.log(a,"+", args);
//     console.log("Type: ", typeof(args))
// };
// myfun3(20,39,50,60)


// // arrow_function with return statement
// var myfun4 = (a,b) => {return a+b};
// console.log(myfun4(56,60));


// // compare arrow_function with function_declaration
// // function declaration
// function myfun5(a,b){
//     return a+b;
// };
// console.log(myfun5(20,50));


// arrow function
var myfun4 = (a,b) => a+b;
console.log(myfun4(30,50));