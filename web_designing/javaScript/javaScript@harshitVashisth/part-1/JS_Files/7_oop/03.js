const obj1 = {
    key1: "value1",
    key2: "value2"
}
const obj2 = {} //empty object
const obj3 = Object.create(obj1); //there is one more way to create empty object

// console.log(obj1);
// console.log(obj2);
// console.log(obj3);

obj1.key3 = "value3"; //adding value
obj2.key4 = "value4";
obj3.key5 = "value5";

// console.log(obj1);
// console.log(obj2);
// console.log(obj3);

/* accessing inherited values */
console.log(obj3.key1);
console.log(obj3.key2);
console.log(obj3.key3);
console.log(obj3.key4);
console.log(obj3.key5);
console.log();

obj3.key3 = "unique"; //obj3 will check first its own value if not found then inherit
console.log(obj3.key3);
console.log();

console.log(obj3.__proto__); //to check inherit and its won values

/*
__proto__ === [[prototype]]

[[prototype]] //official ecmascript documentation
*/
