/* example1 */
/* creating new object */
// const obj1 = {
//     key1: "value1",
//     key2: "value2"
// }

// const obj2 = obj1; //assigning into new variable (it will save into same memory location)

// /* printing both objects */
// console.log(obj1);
// console.log(obj2);

// obj1.key3 = "value3"; //adding a new value (it will effect of both objects)

// console.log(obj1);
// console.log(obj2);




/* example2 (clone object using spread oprator)*/
// const obj1 = {
//     key1: "value1",
//     key2: "value2"
// }

// const obj2 = {...obj1}; //clone into new object (it will save into new memory location)

// /* printing both objects */
// console.log(obj1);
// console.log(obj2);

// obj1.key3 = "value3"; //adding a new value (it will effect only obj object)

// console.log(obj1);
// console.log(obj2);




/* example3 (clone object using object.assign)*/
const obj1 = {
    key1: "value1",
    key2: "value2"
}

const obj2 = Object.assign({}, obj1); //clone into new object (it will save into new memory location)

/* printing both objects */
console.log(obj1);
console.log(obj2);

obj1.key3 = "value4"; //adding a new value (it will effect only obj object)

console.log(obj1);
console.log(obj2);