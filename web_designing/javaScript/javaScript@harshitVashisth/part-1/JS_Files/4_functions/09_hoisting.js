/* hoisting only works with function declairation */

hello("Abdul"); // can be called upside the function

function hello(arg){
    console.log(`Hello ${arg} sir`);
};

hello("Zoha"); // can be called downside the function