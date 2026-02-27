/*
Set: is iterable
It also have its own methods
No index-based access
Order is not guaranteed
Unique items only (no duplicates allowed)
can store any iterables
*/
/* creating Set */
// const items = new Set(); // empty set

const items = new Set("Harshit"); //can store string
const items2 = new Set(["Harshit", "Hameed", "Aarif", "Harshit"]); //can store list
const items3 = new Set([1,2,3,2]); //no duplicates allowed
console.log(items);
console.log(items2);
console.log(items3);