/* example-1 */
// let array1 = ["item-1", "item-2"];
// let array2 = array1;
// console.log(array1 === array2); //to check equality
// console.log("array1 is:",array1); //to print array1
// console.log("array2 is:",array2); //to print array2
// array1.push("item-3"); //to add item
// console.log();

// console.log("array1 is:",array1); //to print array1
// console.log("array2 is:",array2); //to print array2



/* example-2 */
// let array1 = ["item-1", "item-2"];
// let array2 = ["item-1", "item-2"];
// console.log(array1 === array2);
// console.log("array1 is:",array1);
// console.log("array2 is:",array2);
// array1.push("item-3");
// console.log();

// console.log("array1 is:",array1);
// console.log("array2 is:",array2);



/* example-3 */
// let array1 = ["item-1", "item-2"];
// let array2 = array1.slice(0); //to clone array
// console.log(array1 === array2);
// console.log("array1 is:",array1);
// console.log("array2 is:",array2);
// array1.push("item-3");
// console.log();

// console.log("array1 is:",array1);
// console.log("array2 is:",array2);



/* example-4 */
// let array1 = ["item-1", "item-2"];
// let array2 = [].concat(array1); //to clone array
// console.log(array1 === array2);
// console.log("array1 is:",array1);
// console.log("array2 is:",array2);
// array1.push("item-3");
// console.log();

// console.log("array1 is:",array1);
// console.log("array2 is:",array2);



/* example-5 */
// let array1 = ["item-1", "item-2"];
// let array2 = [...array1]; //to clone array
// console.log(array1 === array2);
// console.log("array1 is:",array1);
// console.log("array2 is:",array2);
// array1.push("item-3");
// console.log();

// console.log("array1 is:",array1);
// console.log("array2 is:",array2);



/* example-6 */
let array1 = ["item-1", "item-2"];
console.log("array1 is:",array1);
let array2 = array1.slice(0).concat(["item-3", "item-4"]);
console.log("array2 is:",array2);
console.log(array1 === array2);