/*
The .slice() method extracts a part of a string and returns the extracted part in a new string.
The method takes 2 parameters: the starting index (position), and the ending index (position).
The method returns a string containing the string beginning at the given index upto but not including the character at the index speficied by the second argument.
If a parameter is negative, the position is counted from the end of the string.
*/
var s = "Hi guys let's learn javaScript";
console.log(s);

var sl = s.slice(8, 14);
console.log(sl);