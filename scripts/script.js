function expand(elementId) {
    "use strict";
    var content = document.getElementById(elementId);
    var status = document.getElementById(elementId + "status");
    if (content.className !== "expand") {
        content.className = "expand";
        status.innerHTML = "-";
    } else {
        content.className = "";
        status.innerHTML = "...";
        setTimeout(function () {
            status.innerHTML = "+";
        }, 2000);
    }
}