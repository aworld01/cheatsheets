/* .map() method always returns it's results in array form. */
const numbers = [3,4,6,2,8];

/* callbackFunction (example-1) */
// const square = function(number){
//     return number*number
// }

// const a = numbers.map(square); //returns an array
// console.log(a);


/* callbackFunction (example-2) */
// const a = numbers.map((number, index) => {
//     return `Index: ${index}, ${number*number}`;
// });

// console.log(a);





/* annonymousFunction (example-1) */
// const square = numbers.map(function(number){
//     return number*number
// });
// console.log(square);


/* annonymousFunction (example-1) */
// const square = numbers.map(function(number, index){
//     return `Index: ${index}, Number: ${number}`
// });
// console.log(square);






const users = [
    {firstName: "Harshit", age: 23},
    {firstName: "Mohit", age: 21},
    {firstName: "Nitish", age: 22},
    {firstName: "Garima", age: 20}
]

const userNames = users.map((user)=>{
    return user.firstName;
});
console.log(userNames);