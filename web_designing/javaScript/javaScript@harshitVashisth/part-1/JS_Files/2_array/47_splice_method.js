/*
This method is used to delete items between array
start, number of delete item, insert
*/
/* delete */
// const myArray = ["Item1", "Item2", "Item3", "Item4", "Item5"];
// const deleted = myArray.splice(1, 3); //it returns deleted item
// console.log(myArray);
// console.log(deleted);


/* Insert */
// const myArray = ["Item1", "Item2", "Item3", "Item4", "Item5"];
// myArray.splice(2, 0, "Inserted Item");
// console.log(myArray);


/* Insert and delete */
const myArray = ["Item1", "Item2", "Item3", "Item4", "Item5"];
const deleted = myArray.splice(1, 2, "Inserted Item2", "Inserted Item3");
console.log(myArray);
console.log(deleted); //to check deleted item