let muf = document.getElementById("muf")

document.addEventListener('click', function (event) {
    if (event.target.dataset.btnEdit != undefined) {
        getJsonData(
            event.target.dataset.url,
            { "X-CSRFToken": csrftoken }
        ).then((response) => {
            if (response.includes("textarea")) {
                muf.innerHTML = response
                muf.setAttribute("data-item-id", event.target.dataset.itemId)
            } else {
                window.location.href = "/#mosi";
            }
        })
    }
})
