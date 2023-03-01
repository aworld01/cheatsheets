class Person{
    constructor(fName,lName,age){
        this.fName = fName;
        this.lName = lName;
        this.age = age;
    }
    fullName(){
        console.log(this.fName, this.lName);
    }

    /* static methods is directly releted to class */
    static classInfo(){
        console.log("this is person class")
    }
}

const per1 = new Person("Harshit", "Vashisth");
per1.fullName();
Person.classInfo();
// per1.classInfo(); // it will throw error.