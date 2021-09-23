$.get("https://swapi-api.hbtn.io/api/films/?format=json", function ( data ) {
  const movielist = data.results
  $.each(movielist, function(key, val) {
      $("UL#list_movies").append("<li>" + val.title + "</li>");
      });
});
