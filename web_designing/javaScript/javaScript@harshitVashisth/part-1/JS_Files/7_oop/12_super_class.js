class Animal{
    constructor(name, age){
        this.name = name;
        this.age = age;
    }
    eat(){
        console.log(`${this.name} is eating`);
    }
    isSuperCute(){
        return this.age <= 1;
    }
    isCute(){
        return true
    }
    run(){
        console.log(`${this.name} runs ${this.speed}`);
    }
}

/* drive class */
class Dog extends Animal{
    constructor(name, age, speed){
        super(name, age);
        this.speed = speed;
    }
    
}

const tommy = new Dog("Tommy", 4, "24 kmh");
// tommy.eat();
tommy.run();