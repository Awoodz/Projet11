function nutriFilter(nutrichar, urlDjango, searchProd) {
    $.ajax({
        type: 'GET',
        url: urlDjango,
        data: {
            'nutrichar': nutrichar,
            'search_prod': searchProd,
        },
        success: function (data) {
            var html = $(data).filter('#product_list').html();
            $("#product_list").html(html);
        }
    })
}