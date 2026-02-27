// function about(hobby, job){
//     console.log(`My name is ${this.name} and age is ${this.age}.`);
//     console.log(`My hobby is ${hobby}, and I'm an ${job}`);
// };

// const user1 = {
//     name: "Harshit",
//     age: 18
// }

// let func = about.bind(user1, "Listening to music", "Electrician"); //this will return a function
// func();





const user1 = {
    name: "Harshit",
    age: 28,
    about: function(){
        console.log(this.name, this.age);
    }
}



/* don't do this mistake */
// const myFunc = user1.about;
// myFunc();


/* can do this */
const myFunc = user1.about.bind(user1);
myFunc();