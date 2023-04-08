let students = ["Rahul", "Mahesh", "Abid", "Subhan", "Akbar"];
let myNumbers = [1,2,3,5];
console.log(students);
// console.log(myNumbers);

/* 01: Array.prototype.push()
The push() method adds one or more elements to the end of an array and returns the new length of the array.
*/
// students.push("Rahman"); //to add new element
// console.log(students);

// students.push("Rima", "Rashmi"); //to add multiple arrays
// console.log(students);

// let count = students.push("Rajan"); //to count arrayLength
// console.log(students);
// console.log(count);


/* 02: Array.prototype.unshift()
The unshift() method adds one or more elements to the beginning of an array and returns the new length of the array.
*/
// students.unshift("Rahman"); //to add new element
// console.log(students);

// students.unshift("Rima", "Rashmi"); //to add multiple arrays
// console.log(students);

// let count = students.unshift("Rajan"); //to count arrayLength
// console.log(students);
// console.log(count);

/* example2 */
// myNumbers.unshift(4,6);
// console.log(myNumbers);



/* 03: Array.prototype.pop()
The push() method removes the last element from an array and returns that element.
This method changes the length of the array.
*/

// let poped = students.pop();
// console.log(students);
// console.log(`Poped element => ${poped}`);


/* 02: Array.prototype.shift()
The shift() method removes the first element from an array and returns that removed element.
This method changes the length of the array.
*/
let cont = students.shift(); //to add new element
console.log(students);
console.log(`Shifted element => ${cont}`)

// students.unshift("Rima", "Rashmi"); //to add multiple arrays
// console.log(students);

// let count = students.unshift("Rajan"); //to count arrayLength
// console.log(students);
// console.log(count);