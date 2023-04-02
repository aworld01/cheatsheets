/*
Operator: x++ or ++x or x-- or --x
If use postfix, with operator after operand (for example, x++), the increment operator increaments and returns the value before incrementing.
    var num = 15;
    var newNum = num++;
    console.log(num);
    console.log(newNum);



If use prefix, with operator before oprand (for example, ++x), the increment operator increaments and returns the value after incrementing.
Prefix: increment operator means the variable is incremented first and then the expression is evaluated using the new value of the variable.
example:-
    var num = 15;
    var newNum = ++num;
    console.log(num);
    console.log(newNum);
*/

/* example of postfix */
// var num = 15;
// var newNum = num++;
// console.log(num);
// console.log(newNum);

/* example of prefix */
// var num = 15;
// var newNum = ++num;
// console.log(num);
// console.log(newNum);





/* example of postfix */
var num = 15;
var newNum = num--;
console.log(num);
console.log(newNum);

/* example of prefix */
var num = 15;
var newNum = --num;
console.log(num);
console.log(newNum);