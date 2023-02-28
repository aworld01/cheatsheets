const user = {
    firstName: "Harshit",
    lastName: "Vashistha",
    eMail: "harshitvashisth@gmail.com",
    age: 20,
    address: "houseNumber, Colony, pinCode, state",
    about: function(){
        return `${this.firstName} is ${this.age} years old.`;
    },
    is18: function(){
        return this.age >= 18;
    }
}

const aboutUser = user.about();
// const aboutUser = user.is18();

console.log(aboutUser);