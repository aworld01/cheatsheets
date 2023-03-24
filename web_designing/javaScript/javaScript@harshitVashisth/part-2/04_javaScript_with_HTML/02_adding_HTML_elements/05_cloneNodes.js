const ul = document.querySelector(".todo-list");
const li = document.createElement("li");
li.textContent = "newTodo";

/* example-1 */
// ul.append(li);
// ul.prepend(li);


/* cloneNode */
// const li2 = li.cloneNode(); //to clone only body

const li2 = li.cloneNode(true); //to clone whole node
ul.append(li);
ul.prepend(li2);



/* 5:45:00 / 8:13:32 */