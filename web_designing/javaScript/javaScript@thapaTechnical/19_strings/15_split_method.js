/* A string can be converted to an array with the .split() method */

var txt = "a,b, c, |d,e"; //string

console.log(txt.split(",")); //split on commas
console.log(txt.split(" ")); //split on spaces
console.log(txt.split("|")); //split on pipe