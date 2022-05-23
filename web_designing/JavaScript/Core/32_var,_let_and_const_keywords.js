/*
let
var=variable
const=constant

var: The scope of a variable declared with var is its current execution context, which is either the enclosing function or, for variables declared outside any function, global.

let: let allows you to declare variables that are limited in scope to the block, statement, or expression on which it's used.

const: This declaration creates a constant whose scope can be either global or local the block in which it's declared. Global constants do not become properties of the window object, unlike var variables. An initializer for a constant is required: that is, you must specify its value in the same statement in which it's declared which can't be changed later.
*/

// // var
// function myvar(){
//     var a=10;
//     if(true){
//         var a=20;
//         console.log(a);
//     }
//     console.log(a);
// }
// myvar()


// // var
// for (var i=0; i<5; i++){
//     console.log(i);
// }
// console.log(i)


// // let
// // let name = "Abdul Zoha", // You can't declare variable again, but you can assign variable value.
// function mylet(){
//     let b = 10;
//     if(true){
//         let b = 20;
//         console.log(b);
//     }
//     console.log(b);
// }
// mylet()



// // let
// for (let j=0; j<5; j++){
//     console.log(j);
// }
// console.log(j) // you can't globly accesss variable created by let keyword



// name="Abdul"
// age = 24;
// console.log("Hello", name, "your age is:", age);



const name = "Abdul Zoha"; // const You can't change variable value and you can't assign variable again.
var age = 25;
console.log("Hello", name, "your age is:", age)