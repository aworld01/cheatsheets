/* primitive datatype */
// let num1 = 6;
// let num2 = num1; // (it store in a new heap memory)
// console.log("Value of num1 is:", num1);
// console.log("Value of num1 is:", num1);
// num1++;

// console.log("After incrementing num1");
// console.log("Value of num1 is:", num1);
// console.log("Value of num2 is:", num2);


/* reference datatype */
let array1 = ["item-1", "item-2"];
let array2 = array1; // (it store in same location)
console.log("array1", array1);
console.log("array2", array2);
array1.push("item-3");

console.log("After pushing element to array1");
console.log("array1", array1);
console.log("array2", array2);
