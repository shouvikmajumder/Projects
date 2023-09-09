
var button = document.getElementById("enter")
var input  = document.getElementById("userinput")
var ul = document.querySelector("ul")


function valuelength(){
    if (input.value.length >0){
        return input.value.length 
    }       
}

function lstelement(){
    var li = document.createElement("li");
    li.appendChild(document.createTextNode(input.value));
    ul.appendChild(li);
    input.value = "";
}


function afterclick(){
    if( valuelength()>0){
        lstelement();
    }
}

function afterenter(event) {
    if( valuelength()>0 && event.code === "Enter"){
        lstelement();
    }  
}

button.addEventListener("click",afterclick)

input.addEventListener("keypress", afterenter)