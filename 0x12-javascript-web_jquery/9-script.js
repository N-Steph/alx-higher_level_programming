$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
  const value = data.hello;
  $('DIV#hello').text(value);
});
