let students = ["Rahul", "Mahesh", "Abid", "Subhan", "Akbar"];
let prices = [200, 300, 350, 400, 450, 500, 600];

/*
1: Array.prototype.indexOf()
    Returns the first (least) index of an element within the array equal to an element, or -1 if none is found.
    It search the element from the 0th inex number.
    It's a case sensetive
*/
// console.log(students.indexOf("Abid")); //fetch index of "Abid".
// console.log(students.indexOf("Abid", 3)); //fetch next index after first



/*
2: Array.prototype.lastIndexOf()
    Returns the last (greatest) index of an element within the array equal to an element, or -1 if none is found.
    It search the element last to first.
    It's a case sensetive
*/
// console.log(students.lastIndexOf("Subhan")); //fetch index of "Subhan".
// console.log(students.indexOf("Subhan", 4)); //fetch next index after first



/*
3: Array.prototype.includes()
    Determines whether the array contains a value. Returning true or false as appropriate.
*/
// console.log(students.includes("Abid")); //check if element exists or not.
// console.log(students.includes("Abid", 4)); //check next element after first



/*
4: Array.prototype.find()
    Returns the found element in the array, if some element in the array satisfies the testing function, or undefined if not found.
    Only problem is that it returns only one element.
*/

// const find = prices.find((curVal) => {
//     return curVal < 400;
// });
// console.log(find);


/* example2 */
// console.log(prices.find((curVal) => curVal < 400)); // only one line of code
// console.log(prices.find((curVal) => curVal > 1400)); //returns "undefined"



/*
5: Array.prototype.findIndex()
    Returns the found index in the array, if an element in the array satisfies the testing function, or -1 if not found.
*/
// console.log(prices.findIndex((curVal) => curVal < 400));
// console.log(prices.findIndex((curVal) => curVal > 1400)); //returns "-1"



/*
6: Array.prototype.filter()
    Returns a new array containing all elements of the calling array for which the provided filtering function returns true
*/
const newPrice = prices.filter((element, index) => {
    return element < 400;
});

console.log(newPrice);