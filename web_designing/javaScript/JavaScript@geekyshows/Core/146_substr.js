/*
The .substr() method is similar to slice().
The .substr() method returns the part of a string between the start index and a number of characters after it.
.substr() extracts length characters from a string, counting from the start index. If start is a positive number, the index starts counting at the start iof the string.
If start is a negative number, the index starts counting from the end of the string.
*/
var s = "Hi guys lets learn javaScript";
var find = s.substr(8,8); //s.substr(startingIndex, numberOfCharacters)
console.log(find);
