/*
\n: newline
\': single quote
\": double quote
\\: backslash
\0: the NULL character
\t: tab
\r: carriage return
\v: vertical tab
\b: backslash
\f: form feed
*/

var s1 = "Hello world\nHow are you?";
var s2 = "Hello world\'How are you?";
var s3 = "Hello world\"How are you?";
var s4 = "Hello world\\How are you?";
var s5 = "Hello world\0How are you?";
var s6 = "Hello world\tHow are you?";
var s7 = "Hello world\rHow are you?";
var s8 = "Hello world\vHow are you?";
var s9 = "Hello world\bHow are you?";
var s10 = "Hello world\fHow are you?";

console.log(s10);