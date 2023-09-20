var updModal = document.getElementById("update_modal")
const updateBtn = document.getElementById("btn-update")
var updateTitle = document.getElementsByName("title")
var updateTask = document.getElementsByName("task")
const updateDate = document.getElementsByName("date")
const btnCancel = document.getElementById("close")
const btnEdit = document.querySelectorAll("#edit")

var inputTitle = document.getElementById("input-title"),
    inputDate = document.getElementById("input-date"),
    txtArea = document.getElementById("id_task")

updModal.addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
        if (e.target.nodeName == 'INPUT' && (e.target.type == 'text' || e.target.type == 'date') || (e.target.nodeName == 'TEXTAREA')) {
            const itemId = muf.dataset.itemId
            fetch("item" + "/" + Number(itemId) + "/" + "edit", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                    "X-CSRFToken": csrftoken
                },
                body: new URLSearchParams({
                    title: updateTitle[0].value,
                    task: updateTask[0].value,
                    date: updateDate[0].value
                })
            }).then(async (response) => {
                if (!response.ok) {
                    const text = await response.text()
                    throw new Error(text)
                }
                const djangoUpdForm = await response.text()
                if (djangoUpdForm.includes('class="errorlist"')) {
                    muf.innerHTML = djangoUpdForm
                } else {
                    var modalUpd = bootstrap.Modal.getInstance(updModal)
                    modalUpd.hide();

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

updateBtn.addEventListener("click", function () {
    const itemId = muf.dataset.itemId
    console.log("EDIT", "item" + "/" + Number(itemId) + "/" + "edit")
    fetch("item" + "/" + Number(itemId) + "/" + "edit", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            "X-CSRFToken": csrftoken
        },
        body: new URLSearchParams({
            title: updateTitle[0].value,
            task: updateTask[0].value,
            date: updateDate[0].value
        })
    }).then(async (response) => {
        if (!response.ok) {
            const text = await response.text()
            throw new Error(text)
        }
        const djangoUpdForm = await response.text()
        if (djangoUpdForm.includes('class="errorlist"')) {
            muf.innerHTML = djangoUpdForm
        } else {
            var modalUpd = bootstrap.Modal.getInstance(updModal)
            modalUpd.hide();

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
