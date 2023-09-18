var modal = document.getElementById("delete_modal")
const newPage = document.getElementById("tbl-create")
const delValidator = document.getElementById("del-validator")

delValidator.addEventListener('click', function (event) {
    if (rmf.dataset.itemId != undefined) {
        fetch("item" + "/" + rmf.dataset.itemId + "/" + "delete", {
            method: 'POST',
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken
            }
        }).then(async response => {
            if (response.ok) {
                var modalD = bootstrap.Modal.getInstance(modal)
                modalD.hide();

                const body = document.getElementById("base");
                let div = document.createElement("div")
                div.className = "m-4 alert alert-success float-end position-absolute ad fo top50"
                div.setAttribute('role', "alert")
                let alert = document.createTextNode(`"${response.headers.get("Msg-Status")}"`)
                div.appendChild(alert)
                body.prepend(div)
            } else {
                const text = await response.text()
                throw new Error(text)
            }
        })
    }
})
