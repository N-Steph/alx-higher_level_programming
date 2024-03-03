$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  const films = data.results;
  for (const movie of films) {
    const title = movie.title;
    $(`<li>${title}</li>`).appendTo('UL#list_movies');
  }
});
