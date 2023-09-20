var supModal = document.getElementById("signup-modal")
var signupBtn = document.getElementById("signup-btn")

supModal.addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
        if (e.target.nodeName == 'INPUT' && (e.target.type == 'email' || e.target.type == 'password' || e.target.type == 'text')) {
            fetch(ajax_url_post_signup, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                    "X-CSRFToken": csrftoken
                },
                body: new URLSearchParams({
                    username: suf.parentElement[1].value,
                    email: suf.parentElement[2].value,
                    password1: suf.parentElement[3].value,
                    password2: suf.parentElement[4].value,
                })
            }).then(async (response) => {
                if (!response.ok) {
                    const text = await response.text()
                    throw new Error(text)
                }
                const djangoSupForm = await response.text()
                if (djangoSupForm.includes('class="errorlist"')) {
                    suf.innerHTML = djangoSupForm
                } else {
                    var modalSup = bootstrap.Modal.getInstance(supModal)
                    modalSup.hide();
                    window.location.href = ajax_url_index;
                }
            })
        }
    }
})

signupBtn.addEventListener('click', function (event) {
    fetch(ajax_url_post_signup, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            "X-CSRFToken": csrftoken
        },
        body: new URLSearchParams({
            username: suf.parentElement[1].value,
            email: suf.parentElement[2].value,
            password1: suf.parentElement[3].value,
            password2: suf.parentElement[4].value,
        })
    }).then(async (response) => {
        if (!response.ok) {
            const text = await response.text()
            throw new Error(text)
        }
        const djangoSupForm = await response.text()
        if (djangoSupForm.includes('class="errorlist"')) {
            suf.innerHTML = djangoSupForm
        } else {
            var modalSup = bootstrap.Modal.getInstance(supModal)
            modalSup.hide();
            window.location.href = ajax_url_index;
        }
    })
})