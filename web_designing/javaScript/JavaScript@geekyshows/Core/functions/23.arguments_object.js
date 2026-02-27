// function disp(a,b,c){
//     // console.log("first name: "+a+" middle name: "+b+" last name: "+c);
//     console.log("first name: "+arguments[0]+" last name: "+arguments[2]+" middle name: "+arguments[1]);
// }
// disp("Abdul","Zoha")


// function disp(a,b){
//        arguments[1] = "Samad" // Change argument
//        console.log("first name: "+a+" Last_name: "+b);
//    }
// disp("Abdul","Zoha")



// function disp(a,b,c){
//     var n = arguments.length; //Check length of argument
//     console.log("first name: "+a+" Last_name: "+b+" "+"num: "+c);
//     console.log("Length of the name is:",n);
// }
// disp("Abdul","Zoha",2)



// // Access arguments by for loop
// function disp(){
//     var n = arguments.length;
//     for(var i = 0; i<n; i++){
//         console.log(arguments[i]);
//     }
// }
// disp("Hello","Artificial","World")



function disp(){
        console.log(arguments.callee);
    }
disp()