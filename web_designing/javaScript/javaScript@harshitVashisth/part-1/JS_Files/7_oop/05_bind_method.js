function about(hobby, job){
    console.log(`My name is ${this.name} and age is ${this.age}.`);
    console.log(`My hobby is ${hobby}, and I'm an ${job}`);
};

const user1 = {
    name: "Harshit",
    age: 18
}

let func = about.bind(user1, "Listening to music", "Electrician"); //this will return a function
func();

/* 09:06:00 / 11:08:32 */