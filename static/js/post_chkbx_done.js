async function postJsonData(url, data, headers) {
    try {
        const response = await fetch(url, {
            method: "POST",
            body: JSON.stringify(data),
            headers: headers
        });
        return await response.json();

    } catch (err) {
        return console.warn(err);
    }
}

document.addEventListener('click', function (event) {
    if (event.target.dataset.ckbx != undefined) {
        if (event.target.checked) {
            postJsonData(ajax_url_done, {
                "status": true,
                "item_id": event.target.value,
            }, {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken
            })
                .then(jsonResponse => {
                    let newDone = document.getElementsByTagName("label")
                    for (let i = 0; i < newDone.length; i++) {
                        if (newDone[i].id == event.target.value) {
                            newDone[i].classList.remove("fa-flag")
                            newDone[i].classList.add("fa-check-circle")
                            newDone[i].classList.remove("text-secondary")
                            newDone[i].classList.add("text-success")
                        }
                    }
                })
        } else {
            postJsonData(ajax_url_done, {
                "status": false,
                "item_id": event.target.value,
            }, {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken
            }).then(jsonResponse => {
                let newDone = document.getElementsByTagName("label")
                for (let i = 0; i < newDone.length; i++) {
                    if (newDone[i].id == event.target.value) {
                        newDone[i].classList.remove("fa-check-circle")
                        newDone[i].classList.add("fa-flag")
                        newDone[i].classList.remove("text-success")
                        newDone[i].classList.add("text-secondary")
                    }
                }

            })
        }
    }
})
