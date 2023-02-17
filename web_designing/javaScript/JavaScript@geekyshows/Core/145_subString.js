/*
The .subString() method is similar to slice().
The first argument specifies the index at which the desired subString begins.
The optional second argument indicates the index at which the desired subString ends.
The .method returns a string containing the subString beginning at the given index upto but not including the character at the index speficied by the second argument.
The difference between slice and subString is that subString() can't accept negative indexes.
*/
var s = "Hi guys let's learn javaScript";
var sl = s.substring(8, 14); //14 not included.
console.log(sl);