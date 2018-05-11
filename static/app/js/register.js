$(function () {
    $('#username').change(function () {
        var username = $(this).val();
        $.getJSON('/app/checkuser/', {'username': username}, function (data) {
            $('#username_msg').html(data['msg']);
            if (data['msg'] == '用户名可用') {
                $('#username_msg').css('color', 'green')
            }
            else {
                $('#username_msg').css('color', 'red')
            }
        })
    });
    $('#password,#password_confirm').change(function () {
        var password = $('#password').val();
        if (password.length < 6 | password.length > 16) {
            $('#password_msg').html('密码长度限制(6-16)').css('color', 'red')
        }
        else {
            $('#password_msg').html('密码规范').css('color', 'green')
        }

        var password_confirm = $('#password_confirm').val();

        if (password != password_confirm) {
            $('#password_confirm_msg').html('密码不一致').css('color', 'red')
        }
        else {
            $('#password_confirm_msg').html('密码一致').css('color', 'green')
        }
    })
});

function check() {
    var password = $("#password").val();
    var passwordconfirm = $("#password_confirm").val();
    if (password != passwordconfirm){
        return false;
    }
    var newpassword = md5(password);
    $("#password").val(newpassword);
    return true;
}