$(window).on('load', () => {
  $('DIV#add_item').on('click', () => {
    $('UL.my_list').append('<li>Item</li>');
  });

  $('DIV#remove_item').on('click', () => {
    $('UL.my_list li').get(-1).remove();
  });

  $('DIV#clear_list').on('click', () => {
    const listItem = $('UL.my_list li');
    for (const item of listItem) {
      item.remove();
    }
  });
});
