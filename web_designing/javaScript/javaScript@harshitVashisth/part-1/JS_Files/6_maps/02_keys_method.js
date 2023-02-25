
const person = new Map(); //defining an empty map
// console.log(person);

/* adding items */
person.set("name", "Harshit");
person.set("age", 28);
// console.log(person);


/* example1 */
// let keys = person.keys(); //to get all the keys (we can use loop on this method)
// console.log(keys);


/* example2 */
for(let key of person.keys()){
    console.log(key);
};