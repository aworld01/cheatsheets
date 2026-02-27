function app(){
    console.log("Hello sir, welcome to my world");
    function sum(arg1, arg2){
        return arg1+arg2
    }
    const minus = (arg1, arg2) => {
        return arg1-arg2
    }
    const multi = (arg1, arg2) => arg1*arg2;

    console.log(sum(4,2));
    console.log(minus(5,2));
    console.log(multi(2,5));
}
app();