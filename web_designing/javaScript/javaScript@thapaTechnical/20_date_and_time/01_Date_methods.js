/*
javaScript Date objects represent a single moment in time in a platform-independent format. Date objects contain a Number that represents milliseconds since 1 January 1970 UTC.
There are 4 ways to create a new date object:
    1: new Date()
    2: new Date(year, month, day, hours, minutes, seconds, milliseconds) //it takes 7 arguments
    example:
        var d = new Date(2022, 0, 5, 10, 33, 30, 0);
        console.log(d.toLocaleString())
    3: new Date(milliseconds) //we can't avoid month section
    4: new Date(date string)

Date objects are created with the new Date() constructor.

javaScript counts months form 0-11;
*/

/* example1 */
// let currentDate = new Date();
// console.log(currentDate);
// console.log(currentDate.toLocaleString()); //13/4/2023, 10:31:03 pm
// console.log(currentDate.toString()); //Thu Apr 13 2023 22:33:59 GMT+0300 (Arabian Standard Time)


/* example2 */
// var d = new Date(2022, 0, 5, 10, 33, 30, 0);
// console.log(d.toLocaleString())


/* example3 */
// var d = new Date(2023,4); //we can't avoid month section
// console.log(d);


/* new Date(dateString) creates a new date object from a date string */
// let d = new Date("October 13, 2023 11:13:00");
// console.log(d);
// console.log(d.toLocaleString());


/* example4 */
// let now = Date.now(); //represents milliseconds since 1 January 1970 UTC
// console.log(now);


/* example5 */
let now = new Date();

/* how to get the indivisual date */
// console.log(now.toLocaleString());
// console.log(now.getFullYear()); //to get year
// console.log(now.getMonth()); //to get month 0-1 (jan-Dec);
// console.log(now.getDate()); //to get date
// console.log(now.getDay()); //to get day


/* how to set the indivisual date */
let year = now.setFullYear(2020); //the setFullYear() method can optionally set month and day
let month = now.setMonth(10); //to set month
let date = now.setDate(04); //to set date
let dateAndYear = now.setFullYear(2021, 10, 5); //to set year and date

console.log(now.toLocaleString());