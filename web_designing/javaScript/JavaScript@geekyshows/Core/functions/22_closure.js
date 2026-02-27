/*
Outer function can not access the inner variable.
Inner function can access the outer variable.
*/

function outer(){
    var j = "J is a local variable of outer function";
    console.log(j)
    function inner(){
        var k = "K is a local variable of inner function";
        console.log(k)
        console.log(j)
    }
    inner();
}
outer()