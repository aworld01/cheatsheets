/* example1 */
// function myFunc(){
//     function hello(){
//         return "Hello world"
//     };
//     return hello;
// };

// const ans = myFunc();
// console.log(ans);
// result = ans();
// console.log(result);


/* example2 */
function myFunc(){
    return function hello(){
        return "Hello world"
    };
};

const ans = myFunc();
console.log(ans);
result = ans();
console.log(result);