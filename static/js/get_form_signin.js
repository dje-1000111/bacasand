async function getJsonDataSignin(url, headers) {
    try {
        const response = await fetch(url, {
            method: 'GET',
            headers: headers
        })
        return await response.text()
    } catch (err) {
        return console.warn(err)
    }
}

let sif = document.getElementById("sif")

document.addEventListener('click', function (event) {
    if (event.target.dataset.signin != undefined) {
        event.preventDefault();
        getJsonDataSignin(
            event.target.dataset.urlNext, // get the form at this url and return it in response
            { "X-CSRFToken": csrftoken }
        )

            .then((response) => {
                sif.innerHTML = response
            })
    }
})