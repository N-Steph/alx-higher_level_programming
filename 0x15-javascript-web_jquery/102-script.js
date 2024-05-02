$(window).on('load', () => {
  $('INPUT#btn_translate').on('click', () => {
    const langCode = $('INPUT#language_code').val();
    const URL = 'https://hellosalut.stefanbohacek.dev/' + '?lang=' + langCode;
    $.ajax({
      url: URL,
      success: (data) => {
        $('DIV#hello').text(data.hello);
      },
      dataType: 'json'
    });
  });
});
