function backToIndex() {
    setTimeout(function () {
        getJsonData(
            ajax_url_index,
            { "X-CSRFToken": csrftoken }
        ).then((TextResponse) => {
            newPage.innerHTML = TextResponse
        })
    }, 50)
}

signinBtn.addEventListener("click", backToIndex)