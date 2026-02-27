const person = {
    name: "Harshit",
    age: 22,
    "person hobbies": ["guitar", "sleeping", "listening"]
}

/* for in loop */
// for(let key in person){
//     let val = person[key];
//     console.log(`Key is: ${key}, Value is: ${val}`);
// };

/* Object.keys */
// console.log(Object.keys(person));

for(let key of Object.keys(person)){
    console.log(person[key]);
}