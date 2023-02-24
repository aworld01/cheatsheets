/* example1 */
// const items1 = new Set(); //empty set
// const items2 = new Set("item1");
// console.log(items1);

// items1.add(1); //to stores value in integer.
// items1.add("added item");
// items2.add("added item");
// console.log(items1);
// console.log(items2);


/* example2 */
const numbers = new Set();
const items1 = ["item1", "item2", "item3"];
const items2 = ["item1", "item2", "item3"];
console.log(numbers);

numbers.add(items1);
numbers.add(items2);
numbers.add(["item1", "item2"]);
console.log(numbers);
