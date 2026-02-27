/* beforeend */
const todoList = document.querySelector(".todo-list");
todoList.insertAdjacentHTML("beforeend", "<li>Hello world</li>"); //react like append

/* afterbegin */
todoList.insertAdjacentHTML("afterbegin", "<li>My name is Abdul Zoha") //react like prepend


/* beforebegin */
todoList.insertAdjacentHTML("beforebegin", "<li>Hello world");


/* afterend */
todoList.insertAdjacentHTML("afterend", "<li>How are you</li>");