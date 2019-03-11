$(function () {
    $('.register').width(innerWidth)
});

$(function(){
    // email.click
    $('#email input').blur(function(){
        var reg = new RegExp("^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$");
        if($(this).val()=='') return;

        if(reg.test($(this).val())){
            request_data = {
                'email':$(this).val(),
            };
            $.get('/checkemail/',request_data,function(response){
                if(response.status){
                    $('#email-t').attr('data-content', '账号可用').popover('hide');
                    $('#email').removeClass('has-error').addClass('has-success');
                    $('#email>span').removeClass('glyphicon-remove').addClass('glyphicon-ok');
                }else {
                    $('#email-t').attr('data-content', response.msg).popover('show');
                    $('#email').removeClass('has-success').addClass('has-error');
                    $('#email>span').removeClass('glyphicon-ok').addClass('glyphicon-remove');
                }
            });
        }else{
            $('#email-t').attr('data-content', '格式不正确').popover('show');
            $('#email').removeClass('has-success').addClass('has-error');
            $('#email>span').removeClass('glyphicon-ok').addClass('glyphicon-remove');
        }
    });

    // password.click
    $('#password input').blur(function(){
        var reg = new RegExp("^[0-9a-zA-Z_]{6,10}$");
        if($(this).val()=='') return;

        if($(this).val().length>5 && $(this).val().length<11){
            $('#password-t').popover('hide');
            $('#password').removeClass('has-error').addClass('has-success');
            $('#password>span').removeClass('glyphicon-remove').addClass('glyphicon-ok');
        }else{
            $('#password-t').attr('data-content', '格式不正确').popover('show');
            $('#password').removeClass('has-success').addClass('has-error');
            $('#password>span').removeClass('glyphicon-ok').addClass('glyphicon-remove');
        }
    });

    //verify-psd.click
    $('#verify-psd input').blur(function(){
        if($(this).val()=='') return;

        if($(this).val()==$('#password input').val()){
            $('#verify-psd-t').popover('hide');
            $('#verify-psd').removeClass('has-error').addClass('has-success');
            $('#verify-psd>span').removeClass('glyphicon-remove').addClass('glyphicon-ok');
        }else{
            $('#verify-psd-t').attr('data-content', '密码不一致').popover('show');
            $('#verify-psd').removeClass('has-success').addClass('has-error');
            $('#verify-psd>span').removeClass('glyphicon-ok').addClass('glyphicon-remove');
        }
    });

    //nic-name.click
    $('#nic-name input').blur(function(){
        if($(this).val()=='') return;

        if($(this).val().length>1){
            $('#nic-name-t').popover('hide');
            $('#nic-name').removeClass('has-error').addClass('has-success');
            $('#nic-name>span').removeClass('glyphicon-remove').addClass('glyphicon-ok');
        }else{
            $('#nic-name-t').attr('data-content', '字数太短').popover('show');
            $('#nic-name').removeClass('has-success').addClass('has-error');
            $('#nic-name>span').removeClass('glyphicon-ok').addClass('glyphicon-remove');
        }
    });

    //submit
    $('#subButton').click(function(){
        var flag = true;
        $('.register .form-group').each(function(){
            if($('this').is('has-error')) flag = false;
            else $('.register form').submit();
        });
    });
});