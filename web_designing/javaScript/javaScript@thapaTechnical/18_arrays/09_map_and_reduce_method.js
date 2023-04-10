/* Array.prototype.map()
Returns a new array containing the results of calling a function on every element in this array.
It return new array without mutating the orignal array.
*/
const array1 = [1,4,9,26,25];
console.log(array1);

/* example1 */
// let newArr = array1.map((curElem, index, arr) => {
//     return curElem > 9;
// });
// console.log(newArr);


/* example2 */
// let newArr = array1.map((curElem, index, arr) => {
//     return `Index no = ${index} and the value is ${curElem} belong to ${arr}`
// });
// console.log(newArr);


/* example3 (forEach) */
let newArrFor = array1.forEach((curElem, index, arr) => {
    return `Index no = ${index} and the value is ${curElem} belong to ${arr}`
});
console.log(newArrFor);