const usrs = [
    {usrId: 1, firstName: "Harshit" , gender: "male"},
    {usrId: 2, firstName: "Mohit" , gender: "male"},
    {usrId: 3, firstName: "Nitish" , gender: "female"}
];

/* destructure full details */
// const [usr1, usr2, usr3] = usrs;
// console.log(usr1);


/* example-2 */
// const [{firstName, usrId}, , {fistName, gender}] = usrs;
// console.log(usrId, firstName);
// console.log(firstName, gender);


/* nested destructure */
// const [{firstName}, , {gender}] = usrs;
// console.log(firstName);
// console.log(gender);


/* change variable name */
const [{firstName: v1}, , {gender: g3}] = usrs;
console.log(v1);
console.log(g3);