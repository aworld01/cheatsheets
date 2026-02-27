/* example1 */
// function func1(callback){
//     console.log("Function is doing task1");
//     callback();
// };

// function func2(){
//     console.log("Function is doing task2");
// }

// func1(func2);



/* example2 */
// function func1(callback){
//     console.log("Function is doing task1");
//     callback();
// };

// func1(() => {
//     console.log("function is doing task2")
// });




/* example3 */
// function func1(num1, num2, callback){
//     console.log(num1, num2);
//     callback(num1, num2);
// };

// function add(n1, n2){
//     console.log(n1+n2);
// }

// func1(3,5, add);




/* example4 */
function func1(num1, num2, callback){
    if(typeof num1 === "number" && typeof num2 ==="number"){    
    callback(num1, num2);
    }else{
        console.log("Wrong datatype");
    };
};

function add(n1, n2){
    console.log(n1+n2);
}

func1(3,"8", add);

/* 00:55:00 / 03:49:26 */