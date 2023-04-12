const str = "Apple, Banana, Kiwi";

/*The .substring() method is similar to .slice(). The difference is that substring() can't accept negative indexes.*/
// const res = str.substring(0,4);
// const res2 = str.substring(5,-2);
// console.log(res2);


/* .substr() method is similar to .slice(). The difference is that the secondParameter specifies the length of the extracted part */
const res = str.substr(0,4);
const res2 = str.substr(-4); //to extract 6 character from backside.
console.log(res);