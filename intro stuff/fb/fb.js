
var database = [
    {
    username:"Sho",
    password: "supersecret"},
    {
        username:"Pho",
        password: "supersecret1"},
    {
        username:"Lho",
        password: "supersecret2"}

];

var newsFeed = [
    {
        username :" Bobby",
        timeline: " Hella tired rN"
    },
    {
        username :" Sally",
        timeline: " Hella not tired rN"
    }
];

var Usernameprompt = prompt("whats you username?");
var Passwordprompt = prompt("whats your password");

function isUserValid(username, password){
    for(var i = 0; i < database.length; i++) {
        if (username === database[i].username && password === database[i].password){
            return true;
        }
    }
    return false;
}


function signIN(username,password) {
    if (isUserValid(username,password) === true) {
        console.log(newsFeed);
    }
    else{
        alert("Wrong Username or Password")
    }
}
signIN(Usernameprompt,Passwordprompt)





// var todos = [
//     "cleam room", "brush teeth" , "exercise", "study", "eat healthy"
// ]; 

// for ( var i = 0 ; i<todos.length ; i++) {
//     console.log(todos[i] += "!");
// }

// var count = todos.length

// while(count>=0) {
//     console.log(todos[count])
//     count --
// }