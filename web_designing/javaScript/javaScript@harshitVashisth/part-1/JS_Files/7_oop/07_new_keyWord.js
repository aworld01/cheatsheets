/*
1) It creates an empty object this = {}
2) return this
3) adds into methods
*/

function createUser(name, age){
    this.name = name;
    this.age = age;
}
/* create prototype */
createUser.prototype.about = function(){
    console.log(this.name, this.age);
}

const usr1 = new createUser("Harshit",26);
usr1.about();