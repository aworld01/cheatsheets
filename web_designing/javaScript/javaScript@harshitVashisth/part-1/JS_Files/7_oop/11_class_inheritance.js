class Animal{
    constructor(name, age){
        this.name = name;
        this.age = age;
    }
    eat(){
        return `${this.name} is eating`;
    }
    isSuperCute(){
        return this.age <= 1;
    }
    isCute(){
        return true
    }
}

// const anim = new Animal("Tom",3);
// console.log(anim);
// console.log(anim.eat());

/* drive class */
class Dog extends Animal{
    
}

const dog = new Animal("Tommy", 4);
console.log(dog.eat());