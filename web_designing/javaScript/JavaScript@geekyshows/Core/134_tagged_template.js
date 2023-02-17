/*
Tagged Templates are advanced form of Template literal. Tags allow you to parse template literals with a function. The first argument of a tag function contains an array of string values. The remaining arguments are related to expressions. In the end, your function can return your manipulated string.

21:40 / 32:07
*/

/*
There are 5 movie tickets, each Rs. 200 and if you buy 5 tickets get discount Rs. 50 each.
There are 5 movie tickets, each Rs. 200 and if you buy less than 5 tickets get discount Rs. 0 each.
*/
var noOfTickets = 5;
var buyTickets = 5;
var eachPrice = 200;
var discPrice = 50;

/* template_literal */
// console.log(`There are ${noOfTickets} movie tickets, each Rs. ${eachPrice} and if you buy ${noOfTickets} tickets get discount Rs. ${discPrice} each.`);



/* tagged_literal */
function ticket(theory, nticket, eprice, bticket, dprice){
    // return theory
    // return nticket
    // return eprice
    if(bticket<5){
        dprice = 0;
        return `${theory[0]}${nticket}${theory[1]}${eprice}${theory[2]}${bticket}${theory[3]}${dprice}${theory[4]}`
    }else{
        return `${theory[0]}${nticket}${theory[1]}${eprice}${theory[2]}${bticket}${theory[3]}${dprice}${theory[4]}`
    }
}
console.log(ticket`There are ${noOfTickets} movie tickets each Rs. ${eachPrice} and if you buy ${buyTickets} tickets get discound Rs. ${discPrice} each.`)