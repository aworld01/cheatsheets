/*
ISO 8601 is the international standard for the representation of dates and times.
Year and Month      YYYY-MM                     2018-06
Only Year            YYYY                        2018
Date and Time       YYYY-MM-DDTHH:MM:SSZ        2018-06-21T12:00:00Z
Date and Time       YYYY-MM-DDTHH:MM:SS+HH:MM   2018-06-21T12:00:00+6:30
                    YYYY-MM-DDTHH:MM:SS-HH:MM   2018-06-21T12:00:00-6:30

Date and Time is separated with a capital T.
UTC time is defined with a capital letter Z.
If you want to modify the time relative to UTC, remove the Z and add +HH:MM or -HH:MM instead.
*/

/* example-1 */
// var tarikh1 = new Date("2018-04");
// var tarikh2 = new Date("2018");
// console.log(tarikh1);
// console.log(tarikh2);


/* example-2 */
var tarikh1 = new Date("2018-06-21T12:00:00Z");
var tarikh2 = new Date("2018-06-21T12:00:00+06:30");
var tarikh3 = new Date("2018-06-21T12:00:00-06:30");
console.log(tarikh1);
console.log(tarikh2);
console.log(tarikh3);