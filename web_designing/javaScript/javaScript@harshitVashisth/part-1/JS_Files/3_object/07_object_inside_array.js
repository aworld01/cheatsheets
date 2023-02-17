/* very useful in real world applications */
const usrs = [
    {usrId: 1, firstName: "Harshit" , gender: "male"},
    {usrId: 2, firstName: "Mohit" , gender: "male"},
    {usrId: 3, firstName: "Nitish" , gender: "male"}
];

/* to check all details */
// for(let usr of usrs){
//     console.log(usr);
// };

/* to check userId */
// for(let usr of usrs){
//     console.log(usr.usrId);
// };

/* to check user name */
for(let usr of usrs){
    console.log(usr.firstName);
};