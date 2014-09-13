"use strict";

document.addEventListener("DOMContentLoaded", function (event) {
    var links = document.links;
    for (var i = 0; i < links.length; i++) {
        if (links[i].hostname != window.location.hostname) {
            links[i].target = '_blank';
        }
    }
});

function expand(elementId) {
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