/*
synchronousProgramming vs aSynchronousProgramming
javaScript is a single threaded synchronousProgramming
*/

/* synchronousProgramming example */
// for(let i = 1; i<10000; i++){
//     console.log("inside for loop");
// };

// console.log("script end");




/* setTimeout (example1)*/
// console.log("Script start");

// function hello(){
//     console.log("Hello world!!!");
// }
// setTimeout(hello, 3000); //3000 millisecond = 3 seconds

// console.log("Script end");


/* setTimeout (example2)*/
// console.log("Script start");

// function hello(){
//     console.log("Inside setTimeout");
// }
// setTimeout(hello, 0);

// for(let i = 1; i<100; i++){
//     console.log("......")
// };


/* setTimeout (id)*/
// console.log("Script start");

// function hello(){
//     console.log("Inside setTimeout");
// }
// const id = setTimeout(hello, 0);
// console.log("setTimeout id is: ",id);
// console.log("Script end");


/* setTimeout (use of id)*/
console.log("Script start");

function hello(){
    console.log("Inside setTimeout");
}
const id = setTimeout(hello, 0);
console.log("setTimeout id is: ",id);
console.log("Clearing timeout");
clearTimeout(id); //to clear setTimeOut
console.log("Script end");
/* 00:25:00 / 3:49:26 */