function ajax(dom, path) {
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
        document.getElementById(dom).innerHTML = this.responseText;
    }
    xhttp.open("GET", path);
    xhttp.send();
}
