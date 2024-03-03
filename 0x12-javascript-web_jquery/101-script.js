$(function () {
  $('DIV#add_item').on('click', function () {
    $('<li>Item</li>').appendTo('UL.my_list');
  });

  $('DIV#remove_item').on('click', function () {
    $('UL.my_list Li:last-child').detach();
  });

  $('DIV#clear_list').on('click', function () {
    $('UL.my_list').remove();
  });
});
