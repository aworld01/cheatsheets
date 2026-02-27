function about(hobby, job){
    console.log(`My name is ${this.name} and age is ${this.age}.`);
    console.log(`My hobby is ${hobby}, and I'm an ${job}`);
};

const user1 = {
    name: "Harshit",
    age: 18
}

// about.apply(user1, ["Listening to music", "Electrician"]); //example1

let args = ["Listening to music", "Electrician"];
about.apply(user1, args); //example2