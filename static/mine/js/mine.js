$(function(){
    $('.mine').width(innerWidth);
});

$('#login-a').click(function(){
   $.cookie('back','mine',{exprires:3,path:'/'});
   window.open('/login/', '_self');
});