function add() {
	var1 = document.getElementById("var1").value
	var2 = document.getElementById("var2").value
	result = document.getElementById("result")
	result.innerHTML = parseFloat(var1) + parseFloat(var2)
}

function sub() {
	var1 = document.getElementById("var1").value
	var2 = document.getElementById("var2").value
	result = document.getElementById("result")
	result.innerHTML = parseFloat(var1) - parseFloat(var2)
}

function mul() {
	var1 = document.getElementById("var1").value
	var2 = document.getElementById("var2").value
	result = document.getElementById("result")
	result.innerHTML = parseFloat(var1) * parseFloat(var2)
}

function div() {
	var1 = document.getElementById("var1").value
	var2 = document.getElementById("var2").value
	result = document.getElementById("result")
	result.innerHTML = parseFloat(var1) / parseFloat(var2)
}
