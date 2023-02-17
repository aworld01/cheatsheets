/*
The .search() method searches a string for a specified value and returns the position of the match.
The .search() method can't take a second start position argument.
You can use regularExpration with this method.
It shows first occurance.
*/

var s = "Hi guys let's learn javaScrip";
console.log(s);

var find = s.search("e");
console.log(find);

var find2 = s.search("let's");
console.log(find2);