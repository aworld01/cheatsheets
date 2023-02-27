/* it will find only existing address */
// const user = {
//     name: "Harshit",
//     address: {houseNumber: '1234'}
// }
// console.log(user.name);
// console.log(user.address);
// console.log(user.address.houseNumber);


/* it will find only existing address */
const user = {
    name: "Harshit"
}
console.log(user.name);
console.log(user.address);
console.log(user.address?.houseNumber);