/* String.prototype.replace(searchFor, replaceWith)
The .replace() method replaces a specified value with another value in a string.

Point to remember:-
1: The .replace() method doesn't change the string it is called on. It returns a new string.
2: By default, the .replace() method replaces only the fisrt match.
3: By default, the .replace() method is case sensitive.
 */
const myBioData = "Hello my name is Abdul Zoha and I'm 18. Abdul";
const newBio = myBioData.replace("Abdul", "Samsul");
console.log(myBioData);
console.log(newBio);
