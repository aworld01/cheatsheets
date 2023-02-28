function personInfo(){
    console.log(`Person name is ${this.name} and age is ${this.age}`);
};

const person1 = {
    name: "Harshit",
    age: "8",
    about: personInfo
}

const person2 = {
    name: "Mohit",
    age: "18",
    about: personInfo
}

const person3 = {
    name: "Nitish",
    age: "17",
    about: personInfo
}

// person1.about();
// person2.about();
// person3.about();

// console.log(window); //to get window object (only works in browser)
// console.log(this); //to get window object (only works in browser)

// this === window //works with browser console