$(window).on('load', function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (response) => {
    $('DIV#hello').text(response.hello);
  });
});
