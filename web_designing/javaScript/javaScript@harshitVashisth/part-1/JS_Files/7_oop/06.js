/* the best approch */
function createUser(fName, lName, eMail, age, address){
    const usr = Object.create(createUser.prototype);
    usr.fName = fName;
    usr.lName = lName;
    usr.eMail = eMail;
    usr.age = age;
    usr.address = address;
    return usr;
}

// console.log(createUser.prototype); //to check prototype

createUser.prototype.about = function(){
        return `${this.fName} is ${this.age} years old.`
    }
createUser.prototype.is18 = function(){
    return this.age >= 18;
}

// console.log(createUser.prototype); //to check prototype

const usr1 = createUser("Abdul", "Zoha", "abdulzoha786@gmail.com", 28, "Chandpali");
const usr2 = createUser("Tabassum", "Khatoon", "tabassumkhatoon786@gmail.com", 21, "Mahual");

const user1 = usr1.about(); //calling methods
const user2 = usr2.about();

console.log(user1);
console.log(user2);