const key1 = "objkey1";
const key2 = "objkey2";
const val1 = "myValue1";
const val2 = "myValue2";

/* example-1 */
// const obj = {};
// console.log(obj);

// obj[key1] = val1;
// obj[key2] = val2;
// console.log(obj);


/* example-2 */
const obj = {
    [key1]: val1,
    [key2]: val2
}
console.log(obj);