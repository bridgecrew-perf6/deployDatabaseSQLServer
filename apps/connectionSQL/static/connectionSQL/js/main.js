window.onload = function() {
    let doc = document.getElementById("hover")

    doc.addEventListener("mouseover", function(event){
        event.target.style.color = "purple"

        setTimeout(function() {
            event.target.style.color = "";
        }, 1000);
    }, false);
}