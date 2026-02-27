/* constructor function */

function CreateUser(fName, lName, eMail, age, address){
    // const usr = Object.create(createUser.prototype); //no need
    this.fName = fName;
    this.lName = lName;
    this.eMail = eMail;
    this.age = age;
    this.address = address;
    // return this; //no need
}

CreateUser.prototype.about = function(){
        return `${this.fName} is ${this.age} years old.`
    }
CreateUser.prototype.is18 = function(){
    return this.age >= 18;
}

const usr1 = new CreateUser("Abdul", "Zoha", "abdulzoha786@gmail.com", 28, "Chandpali");
const usr2 = new CreateUser("Tabassum", "Khatoon", "tabassumkhatoon786@gmail.com", 21, "Mahual");

const user1 = usr1.about(); //calling methods
const user2 = usr2.about();

console.log(user1);
console.log(user2);