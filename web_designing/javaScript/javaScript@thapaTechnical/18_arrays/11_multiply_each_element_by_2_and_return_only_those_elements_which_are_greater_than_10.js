const arr = [2, 3, 4, 6, 8];

/* example1 */
// let arr2 = arr.map((curEle) =>{
//     return curEle*2;
// })
// console.log(arr2);


/* example2 */
// let arr2 = arr.map((curElm) => {
//     return curElm * 2;
// }).filter((curElem) => {
//     return curElem > 10;
// })
// console.log(arr2);


/* example3 */
let arr2 = arr.map((curElm) => curElm * 2).filter((curElem) => curElem > 10)
console.log(arr2);