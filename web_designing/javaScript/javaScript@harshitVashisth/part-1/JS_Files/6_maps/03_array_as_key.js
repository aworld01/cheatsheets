const num = new Map();
num.set([1,2,3], "oneTwoThree");
num.set("name", "Harshit")

/* example1 */
// console.log(num.keys());


/* example2 */
// for(let key of num){
//     console.log(key);
// };


/* example3 */
for(let [key, value] of num){
    console.log(`Your key is: ${key} and value is ${value}`);
};