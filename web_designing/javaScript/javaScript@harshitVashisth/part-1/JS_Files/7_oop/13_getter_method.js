/* normalMethod */
// class Person{
//     constructor(fName,lName,age){
//         this.fName = fName;
//         this.lName = lName;
//         this.age = age;
//     }
//     fullName(){
//         console.log(this.fName, this.lName);
//     }
// }

// const per1 = new Person("Harshit", "Vashisth");
// per1.fullName();



/* getterMethod */
class Person{
    constructor(fName,lName,age){
        this.fName = fName;
        this.lName = lName;
        this.age = age;
    }
    get fullName(){
        console.log(this.fName, this.lName);
    }
}

const per1 = new Person("Harshit", "Vashisth");
per1.fullName;