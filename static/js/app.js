//modal box for "about"
var modal = document.querySelector("#description-modal");
var trigger = document.querySelector("#nav1");
var closeButton = document.querySelector("#desc-modal-close-button");

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

document.querySelector("#song-modal-close-button").addEventListener("click", toggleSongModal);

//changing color of chosen moods to white
$("#list li").click(moodClicker);

//adding elements to the list of words with search bar and changing
//their color to white
function addChosenWords() {
    let word = document.querySelector('.moodsInput').value;

    var el = document.getElementById("list");
    var node = document.createElement("li");
    node.innerText = word;
    
    el.appendChild(node);
    node.className = "selected";
    node.addEventListener('click', moodClicker)
}

function selectMood(mood) {
    let moods = window.localStorage.moods
    if (Array.isArray(moods)) {

    } else {
        moods = [mood]
    }
}

//handling "Check your song!" button - saving chosen words to array, POST chosen words,
//showing modal on success
$('.submit').click(function() {
    let moods = $.find('.selected').map(el => el.textContent)
    let csrftoken = $("[name=csrfmiddlewaretoken]").val();
    console.log(moods)
    $.ajax({
      url: "/api/search_song",
      type: "POST",
      headers: {
        "X-CSRFToken": csrftoken
      },
      data: {
          "moods[]": moods
      },
      success:function() {
        alert("Found song");
        document.querySelector('#song-modal').classList.toggle("show-modal");
      }
    })

})

//song result modal
function toggleSongModal() {
    document.querySelector('#song-modal').classList.toggle("show-modal");
}

//changing color of selected moods
function moodClicker() {
    $(this).toggleClass("selected")
}
