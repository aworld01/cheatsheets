/* arrowFunction has no this itself, it takes from its parent. */
const user1 = {
    name: "Harshit",
    age: 18,
    about: () => {
        console.log(this.name, this.age);
    }
}

user1.about();