/*
The isNaN() function is used to determines whether a value is an illegal number (Not-a-Number).
This function returns true if the value equates to NaN. Otherwise it returns false.
This function is different from the Number specific Number.isNaN() method.
The global isNaN() function, converts the tested value to a Number, then tests it.
*/
var a = "50";
var b = 10;
var c = "Hello";

/* example-1 */
// console.log(isNaN(a)); //to check a illegal number.
// console.log(isNaN(b));
// console.log(isNaN(c));



/* example-2 */
// if(isNaN(b)){
//     console.log("Not a number")
// }else{
//     console.log("Legal Number")
// };



/* example-3 */
var x = 50;
var y = "50";
var z = "Hello";

if(isNaN(z)){
    console.log("Not a number")
}else{
    console.log("Legal Number")
};