var sinModal = document.getElementById("mosi")
var signinBtn = document.getElementById("signin-btn")

sinModal.addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
        if (e.target.nodeName == 'INPUT' && (e.target.type == 'email' || e.target.type == 'password')) {
            fetch(ajax_url_post_signin, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                    "X-CSRFToken": csrftoken
                },
                body: new URLSearchParams({
                    email: sif.parentElement[1].value,
                    password: sif.parentElement[2].value,
                })
            }).then(async (response) => {
                if (!response.ok) {
                    const text = await response.text()
                    throw new Error(text)
                }
                const djangoSinForm = await response.text()
                if (djangoSinForm.includes('class="errorlist"') || djangoSinForm.includes('class="errorlist alert alert-danger mt-3"')) {
                    sif.innerHTML = djangoSinForm
                } else {
                    var modalSin = bootstrap.Modal.getInstance(sinModal)
                    modalSin.hide();
                    window.location.href = ajax_url_index; // /!\ TODO: change the url naming and replace index with app
                }
            })
        }
    }
})

signinBtn.addEventListener('click', function (event) {
    event.preventDefault()
    fetch(ajax_url_post_signin, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            "X-CSRFToken": csrftoken
        },
        body: new URLSearchParams({
            email: sif.parentElement[1].value,
            password: sif.parentElement[2].value,
        })
    }).then(async (response) => {
        if (!response.ok) {
            const text = await response.text()
            throw new Error(text)
        }
        const djangoSinForm = await response.text()
        if (djangoSinForm.includes('class="errorlist"') || djangoSinForm.includes('class="errorlist alert alert-danger mt-3"')) {
            sif.innerHTML = djangoSinForm
        } else {
            var modalSin = bootstrap.Modal.getInstance(sinModal)
            modalSin.hide();
            window.location.href = ajax_url_index;
        }
    })
})