function myFunc(){
    console.log("Inside function");
}

function main(callback){ //callback is a convention
    console.log(callback); //printing the function
    callback(); //calling the function
}

main(myFunc);