/*
object reference type
array are good but not sufficient for real world data
object store key value pairs
object don't have index
*/

/* creating objects (example-1) */
// const person = {name: "Harshit", age:24}; //object literal
// console.log(person);

/* creating objects (example-2) */
// const person = {
//     name: "Vashisth",
//     age:25,
//     hobbies: ["guitar", "sleeping", "listening to music"]
// };

/* creating objects (example-3) */
const person = {
    "person name": "Harshit Vashisth",
    age:25,
    "hobbies": ["guitar", "sleeping", "listening to music"] //write in comma if there is space between key
};
console.log(person);
console.log(person.hobbies);
console.log(person["person name"]);


/* accessing data from object (example-1) */
// console.log(person.name);
// console.log(person.age);
// console.log(person.hobbies);

/* accessing data from object (example-2) */
// console.log(person["name"]);
// console.log(person["age"]);
// console.log(person["hobbies"]);


/* adding key value pair to objects (example-1) */
// person.gender = "male";
// console.log(person);

/* adding key value pair to objects (example-2) */
// person["education"] = "12th";
// console.log(person);