// let name = prompt("Enter your Name: ");
// xhttp.open("GET", "https://customer.tahsinayman.repl.co/show/all")
function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}
console.log(JSON.parse(httpGet("https://customer.tahsinayman.repl.co/show/all"))['ID'])
// document.getElementById("name").innerHTML = name;
