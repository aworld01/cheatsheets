/* use const for creating array */

const fruits = ["Apple", "Mango", "Grapes"];

// let i = 0;
// while(i<fruits.length){
//     console.log(fruits[i]);
//     i++;
// }



/* create new array in upperCase */
const fruits2 = []
let i = 0;
while(i<fruits.length){
    let fruit = fruits[i];
    fruit = fruit.toUpperCase();
    fruits2.push(fruit);
    i++;
};
console.log(fruits2);


/* 3:39:50 / 11:08:32 */