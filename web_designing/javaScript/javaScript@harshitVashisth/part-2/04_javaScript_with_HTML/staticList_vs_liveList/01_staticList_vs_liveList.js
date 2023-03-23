/*
querySelector... //gives us static list and not reflect after added items

getElementBy...  //gives us live list and reflect after added items also
*/

const ul = document.querySelector(".todo-list");

const listItems = document.querySelectorAll(".todo-list li"); //gives us staticList

const listItems2 = ul.getElementsByTagName("li"); //gives us liveList

/* adding liveList */
const sixthLi = document.createElement("li");
sixthLi.textContent = "item6";
ul.append(sixthLi);


console.log(listItems);