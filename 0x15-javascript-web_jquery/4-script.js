const toggle = $('DIV#toggle_header');
toggle.addClass('red');
toggle.on('click', () => {
  if (toggle.hasClass('red')) {
    toggle.removeClass('red');
    toggle.addClass('green');
  } else {
    toggle.removeClass('green');
    toggle.addClass('red');
  }
});
