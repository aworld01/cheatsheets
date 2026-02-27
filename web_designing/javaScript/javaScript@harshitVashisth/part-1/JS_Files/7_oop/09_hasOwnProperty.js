/* constructor function */

function CreateUser(fName, lName, eMail, age, address){
    this.fName = fName;
    this.lName = lName;
    this.eMail = eMail;
    this.age = age;
    this.address = address;
}

CreateUser.prototype.about = function(){
        return `${this.fName} is ${this.age} years old.`
    }
CreateUser.prototype.is18 = function(){
    return this.age >= 18;
}

const user1 = new CreateUser("Abdul", "Zoha", "abdulzoha786@gmail.com", 28, "Chandpali");
const user2 = new CreateUser("Tabassum", "Khatoon", "tabassumkhatoon786@gmail.com", 21, "Mahual");

/* to check user1 keys (including prototype) */
// for(let key in user1){
//     console.log(key);
// };


/* to check user1 keys (excluding prototype) */
for(let key in user1){
    if(user1.hasOwnProperty(key)){
        console.log(key);
    }
};