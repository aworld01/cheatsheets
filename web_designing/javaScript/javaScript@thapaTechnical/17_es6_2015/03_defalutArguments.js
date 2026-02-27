/* normalParameters */
// function mult(a,b){
//     return a*b;
// }
// multi = mult(5,3);
// console.log(multi);



/* defaultParameters (example1) */
// function mult(a,b=08){
//     return a*b;
// }

// // var multi = mult(4);
// var multi = mult(5,2);
// console.log(multi);



/* defaultParameters (example2) */
function mult(a=3,b=08){
    return a*b;
}

// var multi = mult();
var multi = mult(5,2);
console.log(multi);