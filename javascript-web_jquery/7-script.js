$.ajax({
        url: "https://swapi-api.hbtn.io/api/people/5/?format=json",
        type: "GET",
        dataType: "json",
        success: function(data) {
            $("DIV#character").text(data.name);
        },
        error: function(error) {
            console.error("Error fetching data:", error);
        }
    });