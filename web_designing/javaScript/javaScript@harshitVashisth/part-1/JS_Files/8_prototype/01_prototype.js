/*
javaScript function === function + object
Only functions provide prototype properties
 */

function hello(){
    console.log("Hello world");
}

/* example1 */
// console.log(hello.name); //to get function name
// hello.myProperty = "very unique value"; //to add your own properties
// console.log(hello.myProperty);
// console.log(hello.prototype); //to check prototype properties


/* example2 */
// if(hello.prototype){
//     console.log("Prototype is present");
// }else{
//     console.log("Prototype is not present");
// }


/* example3 */
console.log(hello.prototype);

/* adding properties */
hello.prototype.abc = "ABC";
hello.prototype.sing = function(){
    return "lalala";
}

console.log(hello.prototype);
console.log(hello.prototype.sing());