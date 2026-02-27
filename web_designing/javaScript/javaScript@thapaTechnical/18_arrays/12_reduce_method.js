/*
flatten an array means to convert the 3d or 2d array into a single dimensional array.

The .reduce() method executes a reducer function (that you provide) on each element of the array, resulting in single output value)

The reducer function takes four arguments:
1: Accumulator
2: currentValue
3: currentIndex
4: sourceArray
*/
/* example1 */
// let arr = [5,6,2];

// let arr2 = arr.reduce((accumulator, curEle, index, arr) =>{
//     return accumulator += curEle;
// })
// console.log(arr2);


/* example2 with initialValue */
// let arr2 = arr.reduce((accumulator, curEle, index, arr) =>{
//     return accumulator += curEle;
// },8) //8 is initialValue
// console.log(arr2);

/* finalExample */
let arr = [2,3,4,6,8];
let arr2 = arr.map((curElm) => curElm * 2).filter((curElem) => curElem > 10).reduce((accumulator, curElem) =>{
    return accumulator += curElem;
})
console.log(arr2);