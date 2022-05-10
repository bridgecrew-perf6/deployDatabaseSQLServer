document.addEventListener("click", function(event){
    document.getElementsByTagName("title")[0].innerHTML = "clicked"

    setTimeout(function() {
        document.getElementsByTagName("title")[0].innerHTML = "Connection"

    }, 1000);
}, false);