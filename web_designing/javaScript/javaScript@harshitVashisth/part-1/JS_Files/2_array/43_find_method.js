/* It finds only first occurence */
// const myArray = ["Hello", "cat", "dog", "lion"];

// function isLength(string){
//     return string.length === 3;
// }

// const result = myArray.find(isLength);
// console.log(result);



/* example2 */
const users = [
    {userId: 1, userName: "Harshit"},
    {userId: 2, userName: "Harsh"},
    {userId: 3, userName: "Nitish"},
    {userId: 4, userName: "Mohit"},
    {userId: 5, userName: "Aaditya"},
];

const myUser = users.find((user)=>user.userId===3);
console.log(myUser);