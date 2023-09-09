var css = document.querySelector('h3')
var c1 = document.querySelector(".color1");
var c2 = document.querySelector(".color2");
var body = document.getElementById("gradient")

function grad(){
	body.style.background = "linear-gradient(to left, " + c1.value + "," + c2.value + ')';
	css.textContent = body.style.background
}

c1.addEventListener("input", grad)

c2.addEventListener("input", grad)



