$(function () {
  $('INPUTbtn_translate').on('click', function () {
    const langCode = ('INPUT#language_code').val();
    const url = 'https://hellosalut.stefanhacek.dev/?lang='.concat(langCode);
    $.get(url, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
