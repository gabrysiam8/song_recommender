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

function changeStyleOfSelectedMoods() {
    let li = document.querySelectorAll('.listOfMoods li');

}

function addChosenWords() {
    let word = document.querySelector('.moodsInput').value;
    console.log(word);

    var el = document.getElementById("list");
    var node = document.createElement("li");
    node.innerText = word;
    el.appendChild(node);
}