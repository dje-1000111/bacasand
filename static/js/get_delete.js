let rmf = document.getElementById("rmf")

document.addEventListener('click', function (event) {
    if (event.target.dataset.btnDelete != undefined) {
        getJsonData(
            "item" + "/" + event.target.dataset.itemId + "/" + "delete",
            { "X-CSRFToken": csrftoken }
        ).then((response) => {
            if (response.includes("détail")) {
                rmf.innerHTML = response
                rmf.setAttribute("data-item-id", event.target.dataset.itemId)
            } else {
                // TODO: send a message to this location to advert about the forced logout
                window.location.href = "/#mosi";
            }
        })
    }
})
