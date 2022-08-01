function users(search) {
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
        console.log(search)
        document.getElementById("users").innerHTML = this.responseText;
    }
    xhttp.open("GET", "http://localhost:80/user/?search=" + search)
    xhttp.send()
}

function callUsers(ele){
    if (ele.value.length >= 2){
        users(ele.value);
    }
}