$(function(){
    $('.cart').width(innerWidth);
});

$(function(){
    total();

    $('.cart .confirm-wrapper').click(function(){
        var $span = $(this).find('span');
        request_data = {
           'cartid': $(this).attr('data-cartid'),
        };
        $.get('/changecartselect/',request_data,function(response){
           if(response.status == 1){
               if(response.isselect) $span.removeClass('no').addClass('glyphicon glyphicon-ok');
               else $span.removeClass('glyphicon glyphicon-ok').addClass('no');
           }
        });
        total();
    });

    // select all
    $('.bill .all').click(function(){
        var isall = $(this).attr('data-all');
        var $span = $(this).find('span');

        isall = (isall == 'false')?true:false;
        $(this).attr('data-all',isall);

        if(isall) $span.removeClass('no').addClass('glyphicon glyphicon-ok');
        else $span.removeClass('glyphicon glyphicon-ok').addClass('no');
        request_data = {
          'isall': isall,
        };
        $.get('/changecartall/', request_data, function (response) {
            if (response.status == 1){
                $('.confirm-wrapper').each(function () {
                    if (isall) $(this).find('span').removeClass('no').addClass('glyphicon glyphicon-ok');
                    else $(this).find('span').removeClass('glyphicon glyphicon-ok').addClass('no');
                    total();
                });
            }
        });
    });

    function total() {
        var sum = 0;
        $('.cart li').each(function () {
            var $confirm = $(this).find('.confirm-wrapper');
            var $content = $(this).find('.content-wrapper');

            if ($confirm.find('.glyphicon').length){
                var price = $content.find('.price').html();
                var num = $content.find('.num').html();
                sum += num * price;
            }
        });
        $('.bill .total b').html(sum);

    }
});

