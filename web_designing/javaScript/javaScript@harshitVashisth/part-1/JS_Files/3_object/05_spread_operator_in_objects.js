const obj1 = {
    key1: "value1",
    key2: "value2"
};
const obj2 = {
    key3: "value3",
    key4: "value4"
};

const newObj1 = {...obj1}
console.log(newObj1);

const newObj2 = {...obj1, ...obj2};
console.log(newObj2);

const newObj3 = {...obj1, ...obj2, key69: "value69"}
console.log(newObj3);

const newObj4 = {...["item1", "item2"]}
console.log(newObj4);



/* 4:23:00 */