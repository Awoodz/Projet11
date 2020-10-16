function nutriFilter(nutrichar, urlDjango) {
    $.ajax({
        type: 'GET',
        url: urlDjango,
        data: {
            'nutrichar': nutrichar
        },
        success: function (data) {
            var html = $(data).filter('#product_list').html();
            $("#product_list").html(html);
        }
    })
}