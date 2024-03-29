$(function(){
    $('.market').width(innerWidth);
})

$(function(){
    var page = $.cookie('page');
    if(page){
        $('.type-slider .type-item').eq(page).addClass('active');
    }else{
        $('.type-slider .type-item:first').addClass('active');
    }
    $('.type-slider .type-item').click(function(){
        // $.cookie('page', $(this).index());
        $.cookie('page', $(this).index(),{exprires:3, path:'/'});
    });
});

$(function(){
    var categoryShow = false;
    $('#category-bt').click(function(){
        categoryShow = !categoryShow;
        categoryShow ? categoryViewShow() : categoryViewHide();
    });
    function categoryViewShow(){
        $('.category-view').show();
        sortViewHide();
        sortShow = false;
        $('#category-bt i').removeClass('glyphicon glyphicon-chevron-up');
        $('#category-bt i').addClass('glyphicon glyphicon-chevron-down');
    }
    function categoryViewHide(){
        $('.category-view').hide();
        $('#category-bt i').removeClass('glyphicon glyphicon-chevron-down');
        $('#category-bt i').addClass('glyphicon glyphicon-chevron-up');
    }
    var sortShow = false;
    $('#sort-bt').click(function () {
        sortShow = ! sortShow;
        sortShow ? sortViewShow() : sortViewHide();
    })
    function sortViewShow(){
        $('.sort-view').show();
        categoryViewHide();
        categoryShow = false;
        $('#sort-bt i').removeClass('glyphicon glyphicon-chevron-up');
        $('#sort-bt i').addClass('glyphicon glyphicon-chevron-down');
    }
    function sortViewHide(){
        $('.sort-view').hide();
        $('#sort-bt i').removeClass('glyphicon glyphicon-chevron-down');
        $('#sort-bt i').addClass('glyphicon glyphicon-chevron-up');
    }
    $('.bounce-view').click(function () {
        sortViewHide();
        sortShow = false;
        categoryViewHide();
        categoryShow = false;
    });
});

$(function () {
    // $('.bt-wrapper .glyphicon-minus').hide();
    // $('.bt-wrapper i').hide();

    // +++++
    $('.bt-wrapper .glyphicon-plus').click(function(){
        request_data = {
            'goodsid': $(this).attr('data-goodsid'),
        };
        var $_th = $(this);
        $.get('/addcart/', request_data, function(response){
            if (response.status == -1) {
                $.cookie('back', 'market', {exprires: 3, path: '/'});
                window.open('/login/', '_self');
            } else if(response.status == 1){
                $_th.prev().html(response.num);
                $_th.prevAll().show();
            }
        });
    });
    $('.bt-wrapper .num').each(function(){
       var num = parseInt($(this).html());
       if(num){
           $(this).prev().show();
           $(this).show();
       }else {
           $(this).prev().hide();
           $(this).hide();
       }
    });

    //-------
    $('.bt-wrapper .glyphicon-minus').click(function(){
        var $_th = $(this);
        request_data = {
            'goodsid': $(this).attr('data-goodsid'),
        };
        $.get('/subcart/', request_data, function(response){
            if (response.status == 1) {
                if(response.num){
                    $_th.next().html(response.num);
                }else {
                    $_th.next().hide();
                    $_th.hide();
                }
            }
        });
    })
});