/* example1 */
// class Person{
//     constructor(fName,lName,age){
//         this.fName = fName;
//         this.lName = lName;
//         this.age = age;
//     }
//     get fullName(){
//         console.log(this.fName, this.lName);
//     }
//     setName(fName,lName){
//         this.fName = fName;
//         this.lName = lName;
//     }
// }

// const per1 = new Person("Harshit", "Vashisth");
// per1.fullName;
// per1.fName = "Abdul";
// per1.lName = "Zoha";
// per1.fullName;





/* example2 */
// class Person{
//     constructor(fName,lName,age){
//         this.fName = fName;
//         this.lName = lName;
//         this.age = age;
//     }
//     get fullName(){
//         console.log(this.fName, this.lName);
//     }
//     setName(fName,lName){
//         this.fName = fName;
//         this.lName = lName;
//     }
// }

// const per1 = new Person("Harshit", "Vashisth");
// per1.fullName;
// per1.setName("Abdul", "Zoha");
// per1.fullName;





/* example3 */
class Person{
    constructor(fName,lName,age){
        this.fName = fName;
        this.lName = lName;
        this.age = age;
    }
    get fullName(){
        console.log(this.fName, this.lName);
    }
    set fullName(name){
        const [firstName, lastName] = name.split(" ")
        this.fName = firstName;
        this.lName = lastName;
    }
}

const per1 = new Person("Harshit", "Vashisth");
per1.fullName;
per1.fullName = "Abdul Zoha";
per1.fullName;