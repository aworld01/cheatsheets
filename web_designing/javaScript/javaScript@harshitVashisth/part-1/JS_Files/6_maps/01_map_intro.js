/*
map is an iterable
stores data in ordered fashion
store key-value pair (like object)
duplicate key are not allowed (like object)


DIFFERENT BETWEEN MAPS AND OBJECTS
OBJECT:-
object can only have string or symbol as key

MAP:-
in map you can use anything as key (like array, number, string)
*/

/* object literal */
const person = {
    name: "Harshit",
    age: 27
}

/* defining map */
const person2 = new Map(); //empty map
// console.log(person2);

/* adding items */
person2.set("Name", "Harshit");
person2.set("age", 27);
person2.set(1, "one");
console.log(person2);

/* accessing items */
let nm = person2.get("Name");
console.log(nm);
console.log(person2.get(1));