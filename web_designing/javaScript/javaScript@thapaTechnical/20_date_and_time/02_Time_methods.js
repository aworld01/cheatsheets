/*
The getTime() method returns the number of milliseconds since January 1, 1970.
The getHours() method returns the hours of a date as a number (0-23)

new Date().toLocaleString() // (14/4/2023, 9:12:23 pm)
new Date().toLocaleTimeString() // (9:12:23 pm)
new Date().toLocaleDateString() // (14/4/2023)
*/
let now = new Date();

/* how to get the indivisual date */
// let time = now.getTime(); //The getTime() method returns the number of milliseconds since January 1, 1970
// let hours = now.getHours(); //The getHours() method returns the hours of a date as a number (0-23)
// let minuts = now.getMinutes(); //to get minutes
// let seconds = now.getSeconds(); //to get milliseconds

// console.log(`Milliseconds since January 1, 1970: ${time}`);
// console.log(`Hours: ${hours}`);
// console.log(`Minuts: ${minuts}`);
// console.log(`Seconds: ${seconds}`);



/* how to get the indivisual date */
// console.log(now.toLocaleString());

// // let time = now.setTime(6,9,12); //learning remain
// let hours = now.setHours(5); //The getHours() method returns the hours of a date as a number (0-23)
// let minuts = now.setMinutes(8); //to get minutes
// let seconds = now.setSeconds(19); //to get milliseconds

// console.log(now.toLocaleString());



/* finalExample */
console.log(new Date().toLocaleString());
console.log(new Date().toLocaleTimeString());
console.log(new Date().toLocaleDateString())