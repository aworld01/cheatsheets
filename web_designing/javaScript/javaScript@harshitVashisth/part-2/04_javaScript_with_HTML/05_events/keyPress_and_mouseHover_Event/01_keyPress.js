const body = document.body;

/* example1 */
// body.addEventListener("keypress", (e) => {
//     console.log(e);
// });


/* example2 */
body.addEventListener("keypress", (e) => {
    console.log(e.key);
});