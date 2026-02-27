let items = ["item1", "item2", "item3", "item4", "item2", "item3", "item1"];
let n = items.length;
console.log(items);
console.log(n);

/* extracting uniqueItems */
const uItmes = new Set(items);
console.log(uItmes);
// let n2 = uItmes.length; //it well thorow undefined value
console.log(n2);

/* to get length */
let n3 = 0;
for(let element of uItmes){
   n3++
}
console.log(n3);