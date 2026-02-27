/*
<body>
    <h1>Events</h1>
    <p class="para">This is a testing demo paragraph.</p>
    <input type="text" class="string"><br>
    <button>clickMe</button>

    <script>
        const para = document.querySelector(".para");
        let btn = document.querySelector("button");
        function show(){
            const input = document.querySelector(".string").value;
            para.innerHTML = input;
        }
        btn.addEventListener("click", show, false);
    </script>
</body>
    
*/