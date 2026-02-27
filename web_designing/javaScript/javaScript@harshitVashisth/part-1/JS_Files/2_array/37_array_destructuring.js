const myArray = ["value1", "value2", "value3", "value4"];

/* example-1 (simpleWay) */
let array1 = myArray[0];
let array2 = myArray[1];
console.log(array1);
console.log(array2);
console.log();


/* example-1 (destructuring) */
// let [var1, var2] = myArray;

// console.log(var1);
// console.log(var2);
// console.log();

// var1 = "valueChanged"; //to change the value
// console.log(var1);
// console.log(var2);


/* example-2 (to skip values) */
// let [var1, , var3] = myArray;

// console.log(var1);
// console.log(var3);


/* example-1 save specific values into new array (simpleWay)*/
// let myArray2 = myArray.slice(2);
// console.log(myArray2);


/* example-2 save specific values into new array (arrayDestructuring)*/
[var1, var2, ...myArray2] = myArray;
console.log(myArray2);