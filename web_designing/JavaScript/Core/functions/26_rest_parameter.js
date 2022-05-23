// function add(...args) //The rest operator must be last paramenter to a function and it returns the value in array...
//     {
//         console.log(args);
//         console.log(args[2])
//     }
// add("Apple",10,20,30);


function add(a, ...args)
    {
        console.log(args);
        console.log("A:", a);
    }
add("Apple",10,20,50);