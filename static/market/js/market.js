$(function(){
    $('.market').width(innerWidth);


})


$(function(){
    var page = $.cookie('page');
    if(page){
        $('.type-slider .type-item').eq(page).addClass('active')
    }else{
        $('.type-slider .type-item').addClass('active');
    }

    $('.type-slider .type-item').click(function(){
        $.cookie('page', $(this).index(),{exprires:3, path:'/'})
    })
})