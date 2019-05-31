//modal box for "about"
var modal = document.querySelector(".modal");
var trigger = document.querySelector("#nav1");
var closeButton = document.querySelector(".close-button");

function toggleModal() {
    modal.classList.toggle("show-modal");
}

function windowOnClick(event) {
    if (event.target === modal) {
        toggleModal();
    }
}

trigger.addEventListener("click", toggleModal);
closeButton.addEventListener("click", toggleModal);
window.addEventListener("click", windowOnClick);

//changing color of chosen moods to white
$("#list li").click(function() {
    if ($(this).css("color") !== "white") {
        ($(this).css("color", "white"));
        ($(this).css("border", "solid 2px white"));
        ($(this).css(":active"));
    }
});

//adding elements to the list of words with search bar and changing
//their color to white
function addChosenWords() {
    let word = document.querySelector('.moodsInput').value;

    var el = document.getElementById("list");
    var node = document.createElement("li");
    node.innerText = word;
    
    el.appendChild(node);
    node.style.color = "white";
    node.style.border = "solid 2px white";
}