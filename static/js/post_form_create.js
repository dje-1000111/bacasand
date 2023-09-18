var createModal = document.getElementById("create_modal")

createModal.addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
        if (e.target.nodeName == 'INPUT' && (e.target.type == 'text' || e.target.type == 'date') || (e.target.nodeName == 'TEXTAREA')) {

            fetch(ajax_url_get_form_create, {
                method: 'POST',
                headers: {
                    "Accept": "application/json",
                    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                    "X-CSRFToken": csrftoken
                },
                body: new URLSearchParams({
                    title: cf.parentElement[1].value,
                    task: cf.parentElement[2].value,
                    date: cf.parentElement[3].value
                })
            }).then(async (response) => {
                if (!response.ok) {
                    const text = await response.text()
                    throw new Error(text)
                }
                const djangoCreateForm = await response.text()
                if (djangoCreateForm.includes('class="errorlist"')) {
                    cf.innerHTML = djangoCreateForm
                } else {
                    var modalCreate = bootstrap.Modal.getInstance(createModal)
                    modalCreate.hide();

                    const body = document.getElementById("base");
                    let div = document.createElement("div")
                    div.className = "m-4 alert alert-success float-end position-absolute ad fo top50"
                    div.setAttribute('role', "alert")
                    let alert = document.createTextNode(`"${response.headers.get("Msg-Status")}"`)
                    div.appendChild(alert)
                    body.prepend(div)
                }
            })
        }
    }
})

validator.addEventListener('click', function (event) {
    fetch(ajax_url_get_form_create, {
        method: 'POST',
        headers: {
            "Accept": "application/json",
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            "X-CSRFToken": csrftoken
        },
        body: new URLSearchParams({
            title: cf.parentElement[1].value,
            task: cf.parentElement[2].value,
            date: cf.parentElement[3].value
        })
    }).then(async (response) => {
        if (!response.ok) {
            const text = await response.text()
            throw new Error(text)
        }
        const djangoCreateForm = await response.text()
        if (djangoCreateForm.includes('class="errorlist"')) {
            cf.innerHTML = djangoCreateForm
        } else {
            var modalCreate = bootstrap.Modal.getInstance(createModal)
            modalCreate.hide();

            const body = document.getElementById("base");
            let div = document.createElement("div")
            div.className = "m-4 alert alert-success float-end position-absolute ad fo top50"
            div.setAttribute('role', "alert")
            let alert = document.createTextNode(`"${response.headers.get("Msg-Status")}"`)
            div.appendChild(alert)
            body.prepend(div)
        }
    })
})
