function nutriFilter(nutrichar, urlDjango, searchProd) {
    $.ajax({
        type: 'GET',
        url: urlDjango,
        data: {
            'nutrichar': nutrichar,
            'search_prod': searchProd,
        },
        success: function (data) {
            console.log(data);
            var html = $(data).filter('#product_list').html();
            console.log(html);
            $("#product_list").html(html);
        }
    })
}