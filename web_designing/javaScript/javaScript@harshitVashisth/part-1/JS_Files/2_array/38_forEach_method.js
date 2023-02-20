// const numbers = [4,2,5,8]

// function myFunc(number, index){
//     console.log(`Index is ${index} number is ${number}`);
// };

/* simple way */
// for(let i=0; i<numbers.length; i++){
//     myFunc(numbers[i], i);
// };

/* smart way */
// numbers.forEach(myFunc);


/* exmaple1 */
// numbers.forEach(function(number, index){
//     console.log(number*2, index);
// })


/* exmaple2 */
// numbers.forEach(function(number){
//     console.log(number*3);
// })



const users = [
    {firstName: "Harshit", age: 23},
    {firstName: "Mohit", age: 21},
    {firstName: "Nitish", age: 22},
    {firstName: "Garima", age: 20}
]

/* example1 (anonymousFunction) */
// users.forEach(function(user){
//     console.log(user.firstName);
// });

/* example2 (arrowFunction) */
// users.forEach((user)=>{
//     console.log(user.firstName);
// });

/* example2 (arrowFunction with index) */
users.forEach((user, index)=>{
    console.log(index, user.firstName);
});