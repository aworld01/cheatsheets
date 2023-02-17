/* 
Immediately_Invoked_Function_Expression(IIFE) in JavaScript
*/

// // Anonymous function
// var a = function(){
//     console.log("This is a Anonymous function...")
// ;}
// a()


// // IIFE
// (function(){console.log("This is a IIFE");})();


// // IIFE with variable
// (function() {
//     var b = "This is a variable..."
//     console.log(b);
// })();


// IIFE with parameter
(function(a){
    console.log(a);
})("This is a parameter example...");