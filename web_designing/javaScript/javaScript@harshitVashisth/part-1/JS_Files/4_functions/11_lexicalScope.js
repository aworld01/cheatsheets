const myVar = "Global"; //first value
function myApp(){
    const myVar = "Father"; //second value
    function myfunc(){
        const myVar = "Son"; //third value
        console.log("inside myFunc", myVar);
    }
    console.log(myVar);
    myfunc();
}

myApp();