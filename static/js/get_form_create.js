let cf = document.getElementById("cf")

document.addEventListener('click', function (event) {
    if (event.target.dataset.launcher != undefined) {
        event.preventDefault();
        getJsonData(
            ajax_url_get_form_create, // get the form at this url and return it in response
            { "X-CSRFToken": csrftoken }
        ).then((response) => {
            if (response.includes("textarea")) {
                cf.innerHTML = response
            } else {
                // TODO: send a message to this location to advert about the forced logout
                window.location.href = "/#mosi";
            }

        })
    }
})