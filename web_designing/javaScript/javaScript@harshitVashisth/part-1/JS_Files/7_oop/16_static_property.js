class Person{
    constructor(fName,lName,age){
        this.fName = fName;
        this.lName = lName;
        this.age = age;
    }
    fullName(){
        console.log(this.fName, this.lName);
    };
    /* static methods is directly releted to class */
    static desc = "this is a static property";
}

const per1 = new Person("Harshit", "Vashisth");
console.log(Person.desc);
console.log(per1.desc) //it will be undefined.