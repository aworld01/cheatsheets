const todoList = document.querySelector(".todo-list");
console.log(todoList);

// console.log(todoList.innerHTML); //to fetch innerHTML


/* example1 (this is only better if you want change the innerHTML) */
// todoList.innerHTML = "<li>New Todo</li>"; //to change innerHTML

// todoList.innerHTML += "<li>New Todo</li>"; //to add new innerHTML




/* example2 (a)*/
// const newTodoItem = document.createElement("li"); //to create new 'li' element
// console.log(newTodoItem);

// const newTodoItemText = document.createTextNode("Hello world"); //to create textNode
// console.log(newTodoItemText);

// newTodoItem.appendChild(newTodoItemText); //to add text into new li

// todoList.append(newTodoItem); //to add into ul



/* example2 (b)*/
const newTodoItem = document.createElement("li"); //to create new 'li' element

newTodoItem.textContent = "Hello world";

// todoList.append(newTodoItem); //to add into last of ul

todoList.prepend(newTodoItem); //to add at first of ul