/* it will make same methods multiple times and occupy much memory */
// function createUser(fName, lName, eMail, age, address){
//     const usr = {};
//     usr.fName = fName;
//     usr.lName = lName;
//     usr.eMail = eMail;
//     usr.age = age;
//     usr.address = address;
//     usr.about = function(){
//         return `${this.fName} is ${this.age} years old.`
//     }
//     usr.is18 = function(){
//         return this.age >= 18;
//     }
//     return usr;
// }

// const usr1 = createUser("Abdul", "Zoha", "abdulzoha786@gmail.com", 28, "Chandpali");
// const usr2 = createUser("Tabassum", "Khatoon", "tabassumkhatoon786@gmail.com", 21, "Mahual");

// console.log(usr1); //it returns an object
// console.log(usr2);

// const user1 = usr1.about(); //calling methods
// const user2 = usr2.about();

// console.log(user1);
// console.log(user2);





/* good approch */
const usrMethods = {
    about: function(){
        return `${this.fName} is ${this.age} years old.`
    },
    is18: function(){
        return this.age >= 18;
    }
}

function createUser(fName, lName, eMail, age, address){
    const usr = {};
    usr.fName = fName;
    usr.lName = lName;
    usr.eMail = eMail;
    usr.age = age;
    usr.address = address;
    usr.about = usrMethods.about;
    usr.is18 = usrMethods.is18;
    return usr;
}

const usr1 = createUser("Abdul", "Zoha", "abdulzoha786@gmail.com", 28, "Chandpali");
const usr2 = createUser("Tabassum", "Khatoon", "tabassumkhatoon786@gmail.com", 21, "Mahual");

const user1 = usr1.about(); //calling methods
const user2 = usr2.about();

console.log(user1);
console.log(user2);