/*
There are 5 movie tickets, each Rs. 200 and if you buy 5 tickets get discount Rs. 50 each.
There are 5 movie tickets, each Rs. 200 and if you buy less than 5 tickets get discount Rs. 0 each.
*/
var noOfTickets = 5;
var buyTickets = 5;
var eachPrice = 200;
var discPrice = 50;


function ticket(theory, ...rest){
    if(rest[2] < 5){
        rest[3] = 0;
        return `${theory[0]}${rest[0]}${theory[1]}${rest[1]}${theory[2]}${rest[2]}${theory[3]}${rest[3]}${theory[4]}`
    }else{
        return `${theory[0]}${rest[0]}${theory[1]}${rest[1]}${theory[2]}${rest[2]}${theory[3]}${rest[3]}${theory[4]}`
    }
}
console.log(ticket`There are ${noOfTickets} movie tickets each Rs. ${eachPrice} and if you buy ${buyTickets} tickets get discound Rs. ${discPrice} each.`);