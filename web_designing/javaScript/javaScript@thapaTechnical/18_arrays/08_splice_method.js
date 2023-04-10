/*
Array.prototype.splice()
Adds and/or removes elements from an array.
example:
    months.splice(startingNumber, deleteCount, string);

1: Add Dec at the end of an array?
2: What is the return value of splice method?
3: update march to March (update)?
4: Delete June from an array?

const months = ['Jan', 'march', 'April', 'June', 'July'];
*/

const months = ['Jan', 'march', 'April', 'June', 'July'];
console.log(months);

/* Add Dec at the end of an array */
// months.splice(5,0,"Dec");
// console.log(months);


/* example2 (dynamic way) */
// months.splice(months.length, 0, "Dec");
// console.log(months);



/* update march to March (update) */
// let ret = months.splice(1, 1, "March");
// console.log(months);
// console.log(`${ret} => March`);


/* example2 (dynamic way) */
// const indexOfMonth = months.indexOf('march');
// if(indexOfMonth != -1){
//     let ret = months.splice(indexOfMonth, 1, "March");
// }else{
//     console.log("No such data found!!!")
// }
// console.log(months);



/* Delete June from an array */
// const indexOfMonth = months.indexOf('June');
// if(indexOfMonth != -1){
//     var ret = months.splice(indexOfMonth, 1);
// }else{
//     console.log("No such data found!!!")
// }
// console.log(months);
// console.log(`Deleted => ${ret}`);



/* Delete all after April */
const indexOfMonth = months.indexOf('June');
if(indexOfMonth != -1){
    var ret = months.splice(indexOfMonth, Infinity);
}else{
    console.log("No such data found!!!")
}
console.log(months);
console.log(`Deleted => ${ret}`);