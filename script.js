const accordionContainer = document.querySelector(".accordion-container")
const accordions = document.querySelectorAll(".accordion-container details")

// What are the possible states when an accordion is clicked:
// There are no open accordions
// There is one open accordion other than the one that is clicked
// There is one open accordion that is the same as the one that is clicked
// Something other than the summary is clicked
accordionContainer.addEventListener("click", (event) => {
    // Clicking on anything other than the summary of an accordion requires no action
    if (event.target.tagName != "SUMMARY"){
        return
    }


    // Without this if-statement it's impossible to close an open accordion
    if (event.target.parentElement.getAttribute("open") == null){
        // It's simpler to close all accordions than to find the open one
        accordions.forEach(accordion => {
            accordion.removeAttribute("open")
        });
    }
    
})