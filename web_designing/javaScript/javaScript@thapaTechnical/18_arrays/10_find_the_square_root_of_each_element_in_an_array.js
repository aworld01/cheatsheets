const arr = [25, 36, 49, 64, 81];

/* example1 */
// let arrSqr = arr.map((curEle) =>{
//     // return curEle;
//     return Math.sqrt(curEle);
// });
// console.log(arrSqr);


/* example2 */
let arrSqr = arr.map((curEle) => Math.sqrt(curEle));
console.log(arrSqr);