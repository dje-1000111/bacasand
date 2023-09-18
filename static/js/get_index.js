function backToIndex() {
    setTimeout(function () {
        getJsonData(
            ajax_url_index,
            { "X-CSRFToken": csrftoken }
        ).then((TextResponse) => {
            const reg1 = /<tbody id\=\"tbl-create\"/g;
            const reg2 = /<\/tbody>/g;
            const begin = TextResponse.search(reg1)
            const end = TextResponse.search(reg2)
            const tbody = TextResponse.slice(begin, end)
            newPage.innerHTML = tbody
        })
    }, 50)
}

validator.addEventListener("click", backToIndex)
updateBtn.addEventListener("click", backToIndex)
btnCancel.addEventListener("keydown", backToIndex)

createModal.addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
        if (e.target.nodeName == 'INPUT'
            && (e.target.type == 'text' || e.target.type == 'date')
            || (e.target.nodeName == 'TEXTAREA')) {
            backToIndex()
        }
    }

})
updModal.addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
        if (e.target.nodeName == 'INPUT'
            && (e.target.type == 'text' || e.target.type == 'date')
            || (e.target.nodeName == 'TEXTAREA')) {
            backToIndex()
        }
    }

})

delValidator.addEventListener("click", backToIndex)
