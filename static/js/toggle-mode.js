/* Based on https://codepen.io/brianhaferkamp/pen/WNrJmZb
Original work in 
 - html (PUG)
 - css (Sass)
 - js (JQuery)

 Goal: adapt it in vanilla.
*/
if (document.getElementById("table")) {
    var table = document.getElementById("table")
}
if (document.getElementById("bas")) {
    var bas = document.getElementById("bas")
}

let ligbtn = document.getElementById("ligbtn")
let darkBtn = document.getElementById("darkbtn")
// Dark Mode Setup
var darkMode;
if (localStorage.getItem('dark-mode')) {
    // if dark mode is in storage, set variable with that value
    darkMode = localStorage.getItem('dark-mode');
} else {
    // if dark mode is not in storage, set variable to 'light'
    darkMode = 'light';
}
// set new localStorage value
localStorage.setItem('dark-mode', darkMode);


if (localStorage.getItem('dark-mode') == 'dark') {
    // if the above is 'dark' then apply .dark to the body
    body = document.body
    body.classList.toggle("dark-mode");
    // hide the 'dark' button
    darkBtn.hidden = true
    // show the 'light' button
    ligbtn.hidden = false
    // show the dark table
    if (document.getElementById("table")) {
    table.classList.remove("table-light")
    table.classList.add("table-dark")
    }
    if (document.getElementById("bas")) {
        bas.classList.remove("bg-light")
        bas.classList.add("bg-dark-subtle")
        }

}

// Toggle dark UI

darkBtn.addEventListener("click", function (e) {
    if (e.target.hidden === false) {
        darkBtn.hidden = true
        ligbtn.hidden = false
        body = document.body
        body.classList.toggle("dark-mode");
        if (document.getElementById("table")) {
        table.classList.remove("table-light")
        table.classList.add("table-dark")
        }
        if (document.getElementById("bas")) {
            bas.classList.remove("bg-light")
            bas.classList.add("bg-dark-subtle")
            }

        localStorage.setItem('dark-mode', 'dark');
    }
})
ligbtn.addEventListener("click", function (e) {
    if (e.target.hidden === false) {
        ligbtn.hidden = true
        darkBtn.hidden = false
        body = document.body
        body.classList.toggle("dark-mode");
        if (document.getElementById("table")) {
        table.classList.remove("table-dark")
        table.classList.add("table-light")
        }
        if (document.getElementById("bas")) {
            bas.classList.remove("bg-dark-subtle")
            bas.classList.add("bg-light")
            }
        localStorage.setItem('dark-mode', 'light');
    }
})


// ---------------------ORIGINAL------------------------//

// if (localStorage.getItem('dark-mode') == 'dark') {
//     // if the above is 'dark' then apply .dark to the body
//     $('body').addClass('dark');  
//     // hide the 'dark' button
//     $('.dark-button').hide();
//     // show the 'light' button
//     $('.light-button').show();
//   }
  
  
//   // Toggle dark UI
  
//   $('.dark-button').on('click', function() {  
//     $('.dark-button').hide();
//     $('.light-button').show();
//     $('body').addClass('dark');  
//     // set stored value to 'dark'
//     localStorage.setItem('dark-mode', 'dark');
//   });
  
//   $('.light-button').on('click', function() {  
//     $('.light-button').hide();
//     $('.dark-button').show();
//     $('body').removeClass('dark');
//     // set stored value to 'light'
//     localStorage.setItem('dark-mode', 'light');   
//   });
  
  
  
  //--------------------------------------------------
  // Below is all that is neede for the basic toggle
  //--------------------------------------------------
  
  // $('.dark-button').on('click', function() {  
  //   $('.dark-button').hide();
  //   $('.light-button').show();
  //   $('body').addClass('dark');
  // });
  
  // $('.light-button').on('click', function() {  
  //   $('.light-button').hide();
  //   $('.dark-button').show();
  //   $('body').removeClass('dark');  
  // });