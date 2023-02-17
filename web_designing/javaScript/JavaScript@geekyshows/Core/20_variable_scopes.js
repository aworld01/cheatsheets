/* 
If there is function inside a function the inner function can access outer function's variables but outer function can not access inner function's variables.

There are two types of variable
1.Global_variable
You can accessese it from anywhere.
A variable that is declared outside a function is called Global_variable.
If a variable has not been declared with var it is created as a global_variable.

2.Local_variable
You can only access in any specific function
A variable that is declared inside a function definition is a local_variable.
*/

// // GLOBAL VAR
// var str = "I am global variable"; //Global variable
// function show(){
//     console.log("in func:", str); //inside a function
// }
// show()

// console.log("out func:", str); //outside a function

// if(true){
//     console.log("in block:", str); //inside a block
// }

// // If a variable has not been declared with var it is created as a global_variable.
// function show(){
//     str = "I am global variable"; //Global variable
//     console.log("in func:", str); //inside a function
//     }
// show()
// console.log("out func:", str); //outside a function

// if(true){
//     console.log("in block:", str); //inside a block
// }


// LOCAL_VAR
function show(){
    var str = "I am local variable"; //Local variable
    console.log("in func:", str);
}
show()