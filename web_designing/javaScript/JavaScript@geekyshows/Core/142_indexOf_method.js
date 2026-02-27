/*
The indexOf() method takes a string argument and returns the index of the first occurance of the argument in the string. If the argument is not found returns -1. This method also accepts an optional second argument that specifies the index at which to start the search.
The indexOf() method can't take powerful search values (regular expressions).
*/
var s = "Hi guys let's learn javaScript";
var n = s.indexOf("e"); //This will search first occurance
var n2 = s.indexOf("e", 10); //This will search from 10th index
var n3 = s.indexOf("let's"); //This will search a complete world index

console.log(n);
console.log(n2);
console.log(n3);