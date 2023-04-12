/*
There are three methods to extract the string:-
    .slice(start, end)
    .substring(start, end)
    .substr(start, end)

The .slice() method extracts a part of a string and returns the extracted part in a new string.

The .slice() method selects the elements starting at the given start argument, and ends at, but does not inclued, the given and argument.

Note: The original array will not be changed.
*/

const about = "My name is Abdul Zoha";
const str = "Apple, Banana, Kiwi";

/* example1 */
// let res = str.slice(0,4);
// console.log(res);

/* example2 */
// let res = str.slice(4,-2);
// console.log(res);

/* example3 */
let res = str.slice(4);
console.log(res);