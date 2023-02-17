/* 
Function expression in JavaScript are not hoisted, unlike fucntion declarations.
You can't call function expression before function definition.
*/


/* function declaration */
// show() //You can call function declaration before function definition.
// function show(){
//     console.log("ArtificialWorld...")
// }


/* function expression */
// var disp = function show(){
//     console.log("ArtificialWorld...")
// }
// disp() //You can't call function expression before function definition.