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
    })
});