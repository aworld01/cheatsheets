/*
let and const are block scope
var is function scope
*/
/* blockScope */
// {
//     let firstName = "Abdul";
//     console.log(firstName);
// }

// // console.log(firstName); // can't be access from outside the block

// {
//     let firstName = "Zoha";
//     console.log(firstName);
// }

// let firstName = "Abdul Zoha";
// console.log(firstName);




/* functionScope */
{
    var firstName = "Abdul";
    console.log(firstName);
}

console.log(firstName); // can be access from anywhere

{
    console.log(firstName);
}

var firstName = "Abdul Zoha"; //can be re-assign
console.log(firstName);