$.ajax({
        url: "https://swapi-api.hbtn.io/api/films/?format=json",
        type: "GET",
        dataType: "json",
        success: function(data) {
            $("UL#list_movies").text(data.title);
        },
        error: function(error) {
            console.error("Error fetching data:", error);
        }
    });