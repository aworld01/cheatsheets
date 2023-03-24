/*
appendChild;
insertBefore;
replaceChild;
removeChild;
*/
const ul = document.querySelector(".todo-list");

/* appendChild */
// const li = document.createElement("li");
// li.textContent = "appendChild";
// ul.appendChild(li);


/* insertBefore */
// const referenceNode = document.querySelector(".firstTodo");
// const li2 = document.createElement("li");
// li2.textContent = "insertBefore";
// ul.insertBefore(li2, referenceNode);


/* insertBefore */
// const referenceNode = document.querySelector(".firstTodo");
// const li2 = document.createElement("li");
// li2.textContent = "replaceChild";
// ul.replaceChild(li2, referenceNode);


/* removeChild */
const referenceNode = document.querySelector(".firstTodo");
const li2 = document.createElement("li");
li2.textContent = "removeChild";
ul.removeChild(referenceNode);