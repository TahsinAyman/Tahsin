function signup() {
    email = document.getElementById("email").value
    pass = document.getElementById("password").value

    if (email == "mail4tahsin@gmail.com" && pass == "skyout123") {
        alert("Valid Login Details");
    } else {
        alert("Invalid Login Details");
    }
}
