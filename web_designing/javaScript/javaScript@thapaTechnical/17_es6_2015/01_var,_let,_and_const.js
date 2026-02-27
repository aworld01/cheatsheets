/*
var
===
can change the same variable
can make a new variable with the same name
supports functionScope


let
===
can change the same variable
can't make a new variable with the same name (this will throw errors)
supports blockScope


const
=====
can't change the same variable (this will throw errors)
can't make a new variable with the same name (this will throw errors)
supports blockScope
*/

/* var example*/
// var name = "Abdul";
// name = "Zoha"; //can change the same variable
// var name = "Abdul Zoha"; // can make a new variable with the same name


/* let example*/
// let name = "Abdul";
// name = "Zoha"; //can change the same variable
// var name = "Abdul Zoha"; // can't make a new variable with the same name (this will throw errors)


/* const example*/
// const name = "Abdul";
// name = "Zoha"; //can't change the same variable
// var name = "Abdul Zoha"; // can't make a new variable with the same name (this will throw errors)

// console.log(name);





/* example of var (functionScope) */
// function biodata(){
//     var myFirstName = "Abdul";
//     console.log(myFirstName);

//     if(true){
//         var myLastName = "Zoha";
//         console.log("Inner:", myLastName);
//         console.log("Inner:", myFirstName);
//     }
//     console.log("InnerOuter", myLastName)
// }

// biodata()



/* example of let, const (blockScope) */
function biodata(){
    let myFirstName = "Abdul";
    console.log(myFirstName);

    if(true){
        let myLastName = "Zoha";
        console.log("Inner:", myLastName);
        console.log("Inner:", myFirstName);
    }
    // console.log("InnerOuter", myLastName); //cant access outside of block
}

biodata()
// console.log(myFirstName); //cant access outside of block