$.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    succes: (movies) => {
        $.each(movies.result, function (1, movie) {
	    $("#list_movies).text(movie.title)
	})
    }
});
