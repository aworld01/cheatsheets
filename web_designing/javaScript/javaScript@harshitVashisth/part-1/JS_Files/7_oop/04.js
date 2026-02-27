// const obj1 = {key1: "value1", key2: "value2"}
// const obj2 = Object.create(obj1);

// console.log(obj1);
// console.log(obj1);
// console.log();

// console.log(obj1.__proto__);
// console.log(obj2.__proto__);





/* very good approch */
const usrMethods = {
    about: function(){
        return `${this.fName} is ${this.age} years old.`
    },
    is18: function(){
        return this.age >= 18;
    }
}

function createUser(fName, lName, eMail, age, address){
    const usr = Object.create(usrMethods);
    usr.fName = fName;
    usr.lName = lName;
    usr.eMail = eMail;
    usr.age = age;
    usr.address = address;
    return usr;
}

const usr1 = createUser("Abdul", "Zoha", "abdulzoha786@gmail.com", 28, "Chandpali");
const usr2 = createUser("Tabassum", "Khatoon", "tabassumkhatoon786@gmail.com", 21, "Mahual");

const user1 = usr1.about(); //calling methods
const user2 = usr2.about();

console.log(user1);
console.log(user2);