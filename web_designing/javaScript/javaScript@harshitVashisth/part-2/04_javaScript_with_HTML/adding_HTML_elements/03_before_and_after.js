const newTodoItem = document.createElement("li");
console.log(newTodoItem);

const todoList = document.querySelector(".todo-list");
console.log(todoList); //to select 'todo-list' class

newTodoItem.textContent = "Hello world"; //to add text into list

// todoList.before(newTodoItem); //to add at before

// todoList.after(newTodoItem); //to add after