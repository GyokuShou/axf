$(function(){
    $('.cart').width(innerWidth);
});

$(function(){
    $('.cart .confirm-wrapper').click(function(){
       request_data = {
           'cartid': $(this).attr('data-cartid'),
       };
       console.log(request_data.cartid);
       $.get('/changecartselect/',request_data,function(response){
           console.log(response)
       })
    });
});