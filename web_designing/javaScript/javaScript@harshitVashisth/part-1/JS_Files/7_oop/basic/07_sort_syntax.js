const user1 = {
    name: "Harshit",
    age: 28,
    about: function(){
        console.log(this.name, this.age);
    }
}

const user2 = {
    name: "Abdul Zoha",
    age: 29,
    about(){
        console.log(this.name, this.age);
    }
}

user1.about();
user2.about();