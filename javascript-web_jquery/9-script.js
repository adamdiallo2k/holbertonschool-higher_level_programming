$(document).ready(function() {
    $.ajax({
        url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
        type: "GET",
        dataType: "json",
        success: function(data) {
            $("DIV#hello").text(data.hello);
        },
        error: function(error) {
            console.error("Error fetching data:", error);
        }
    });
});