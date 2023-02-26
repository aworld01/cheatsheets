/* object */
const person1 = {
    id: 1,
    name: "Harshit",
}

/* map */
const extraInfo = new Map();
extraInfo.set(person1, {age: 8, gender: "male"});
// console.log(extraInfo); //to see map

console.log(person1.id); //to see id
console.log(extraInfo.get(person1)); //to get person1 values
console.log(extraInfo.get(person1).gender);