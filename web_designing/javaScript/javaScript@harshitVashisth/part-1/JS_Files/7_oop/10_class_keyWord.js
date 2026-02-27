/* example1 */
// function CreateUser(fName, lName, eMail, age, address){
//     this.fName = fName;
//     this.lName = lName;
//     this.eMail = eMail;
//     this.age = age;
//     this.address = address;
// }

// CreateUser.prototype.about = function(){
//         return `${this.fName} is ${this.age} years old.`
//     }
// CreateUser.prototype.is18 = function(){
//     return this.age >= 18;
// }

// const user1 = new CreateUser("Abdul", "Zoha", "abdulzoha786@gmail.com", 28, "Chandpali");
// const user2 = new CreateUser("Tabassum", "Khatoon", "tabassumkhatoon786@gmail.com", 21, "Mahual");





/* example2 */
class CreateUser{
    constructor(fName, lName, eMail, age, address){
        console.log("Constructor called..")
        this.fName = fName;
        this.lName = lName;
        this.eMail = eMail;
        this.age = age;
        this.address = address;
    }
    about(){
        return `${this.fName} is ${this.age} years old.`
    }
    is18(){
        return this.age >= 18;
    }
    sing(){
        return "la la la la";
    }
    func(a,b){
        return a+b
    }
}

const user1 = new CreateUser("Abdul", "Zoha", "abdulzoha786@gmail.com", 28, "Chandpali");
const user2 = new CreateUser("Tabassum", "Khatoon", "tabassumkhatoon786@gmail.com", 21, "Mahual");

// console.log(user1.about()); //to call methods
// console.log(user2.about());

// console.log(user1.fName); //to get firstName

console.log(Object.getPrototypeOf(user1)); //to check prototype
console.log(user1.func(4,5));