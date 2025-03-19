const accordionContainer = document.querySelector(".accordion-container")
const accordions = document.querySelectorAll(".accordion-container details")

accordionContainer.addEventListener("click", (event) => {
    if (event.target.tagName != "SUMMARY") {
        return
    }

    closeAllOthers(event.target.parentElement)
})

function closeAllOthers(currentElement) {
    for(const accordion of accordions){
        if (accordion === currentElement) {
            continue
        }

        accordion.removeAttribute("open")
    }
}

