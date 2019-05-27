$(document).ready(function() {

    $(function() {
      $("#moods").autocomplete({
        source: "/api/get_moods",
        minLength: 2,
      });
    });

});