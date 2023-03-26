const todoForm = document.querySelector(".form-todo");
const todoInput = document.querySelector(".form-todo input[type='text']"); //to select input field
const todoList = document.querySelector(".todo-list");

/* example1 */
// todoForm.addEventListener("submit", (e) =>{
//     e.preventDefault(); //to stop page refreshing
//     console.log(todoInput.value); //to get value
//     todoInput.value = ""; //to clear value
// });



/* example2 */
todoForm.addEventListener("submit", (e) =>{
    e.preventDefault();
    const newTodoText = todoInput.value;
    const newLi = document.createElement("li");
    const newLiInnerHtml = `<span class="text">${newTodoText}</span>
    <div class="todo-buttons">
        <button class="todo-btn done">Done</button>
        <button class="todo-btn remove">Remove</button>
    </div>`;
    newLi.innerHTML = newLiInnerHtml;
    todoList.append(newLi)
    todoInput.value = "";
});

/* 8:05:00 / 8:13:32 */