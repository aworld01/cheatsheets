// for(let i=0; i<=9; i++){
//     console.log(i);
// }

let fruits = ["apple", "banana", "mango", "grapes"];

// console.log(fruits[2]); //to access 3rd element

// let n = fruits.length; //to get length of array
// console.log(n);


/* to get last element */
// let last = fruits.length-1;
// console.log(fruits[last]);



/* forLoop in array */
// let n = fruits.length
// for(let i=0; i<n; i++){
//     console.log(fruits[i]);
// }



/* forLoop in array */
// let n = fruits.length
// for(let i=0; i<n; i++){
//     var fruit = fruits[i];
//     var fruit = fruit.toUpperCase();
//     console.log(fruit);
// }



/* create new array in upperCase */
let fruits2 = []; // an empty array
console.log(fruits2); //to print empty array

let n = fruits.length
for(let i=0; i<n; i++){
    var fruit = fruits[i];
    var fruit = fruit.toUpperCase()
    fruits2.push(fruit);
}

console.log(fruits2); //to print updated array