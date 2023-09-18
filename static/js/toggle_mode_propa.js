if (document.getElementById("bas")) {
    var bas = document.getElementById("bas")
}

let ligbtn = document.getElementById("ligbtn")
let darkBtn = document.getElementById("darkbtn")

var darkMode;
if (localStorage.getItem('dark-mode')) {
    darkMode = localStorage.getItem('dark-mode');
} else {
    darkMode = 'light';
}
localStorage.setItem('dark-mode', darkMode);

tables = document.querySelectorAll("#table")

if (localStorage.getItem('dark-mode') == 'dark') {
    body = document.body
    body.classList.toggle("dark-mode");
    darkBtn.hidden = true
    ligbtn.hidden = false
    tables.forEach(table => {
        table.classList.remove("table-light")
        table.classList.add("table-dark")
    });

    if (document.getElementById("bas")) {
        bas.classList.remove("bg-light")
        bas.classList.add("bg-dark-subtle")
    }
}

darkBtn.addEventListener("click", function (e) {
    if (e.target.hidden === false) {
        darkBtn.hidden = true
        ligbtn.hidden = false
        body = document.body
        body.classList.toggle("dark-mode");
        tables.forEach(table => {
            table.classList.remove("table-light")
            table.classList.add("table-dark")
        });

        if (document.getElementById("bas")) {
            bas.classList.remove("bg-light")
            bas.classList.add("bg-dark-subtle")
        }
        localStorage.setItem('dark-mode', 'dark');
    }
});

ligbtn.addEventListener("click", function (e) {
    if (e.target.hidden === false) {
        ligbtn.hidden = true
        darkBtn.hidden = false
        body = document.body
        body.classList.toggle("dark-mode");
        tables.forEach(table => {
            table.classList.remove("table-dark")
            table.classList.add("table-light")
        });

        if (document.getElementById("bas")) {
            bas.classList.remove("bg-dark-subtle")
            bas.classList.add("bg-light")
        }
        localStorage.setItem('dark-mode', 'light');
    }
});
