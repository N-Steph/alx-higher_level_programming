$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (response) => {
  const result = response.results;
  for (const index of result) {
    $('UL#list_movies').append('<li>' + index.title + '</li>');
  }
  $('DIV#character').text(response.name);
});
