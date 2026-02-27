let str = "HELLO WORLD";

/* The charCodeAt() method returns the unicode of the character at a specified index in a string.
This method returns a UTF-16 code (an integer between 0-65535).
The unicode Standard provides a unique number for every character, no matter the platform, device, application, or language. UTF-8 is a popular Unicode encoding which has 88-bit code units. */

/* example1 */
// console.log(str.charCodeAt(0));


/* Return the Unicode of the last character in a string */
// let lastChar = str.length -1;
// console.log(str.charCodeAt(lastChar));



/* ECMAScript5 (2009) allows property access [ ] on strings */
console.log(str[6]);