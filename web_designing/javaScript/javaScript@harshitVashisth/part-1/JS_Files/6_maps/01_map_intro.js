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

/* map */
const person2 = new Map();
console.log(person2);

/* adding items */
person2.set("Name", "Harshit");
console.log(person2);

/* 8:16:00 / 11:08:32 */