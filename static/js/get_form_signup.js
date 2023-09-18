async function getJsonData(url, headers) {
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

let suf = document.getElementById("suf")

document.addEventListener('click', function (event) {
    if (event.target.dataset.signup != undefined) {
        event.preventDefault();
        getJsonData(
            event.target.dataset.urlSignup, // get the form at this url and return it in response
            { "X-CSRFToken": csrftoken }
        )

            .then((response) => {
                suf.innerHTML = response
            })
    }
})