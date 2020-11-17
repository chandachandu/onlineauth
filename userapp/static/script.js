$(document).ready(function () {
    $("form#userloginform").submit(function (e) {
        e.preventDefault();
        $('.error_text').remove();
        var dataerror=0;
        var user=$('#userid').val().trim()
        var pwd=$('#userPassword').val().trim()
        if(user.length == 0){
            $('#userid').after('<span class="error_text text-danger">Please Enter User ID</span>');
            dataerror=1;
        }
        if(pwd.length == 0){
            $('#userPassword').after('<span class="error_text text-danger">Please Enter Password</span>');
            dataerror=1;

        }
        if(!dataerror){

            var data=$(this).serialize();
            var url = $(this).attr('action');
            var host=window.location.host;
            $.ajax({
                url:url,
                type:"POST",
                data:data,
                beforeSend:function (data) {
                    $("#userloginform").addClass('overlay')
                    $("#userloginform").after("<img src='static/images/ajax-loader.gif' class='overlay-loader'>");
                },
                success:function (data) {
                    setTimeout(function () {
                          $("#userloginform").removeClass('overlay');
                          $('.overlay-loader').remove();
                          if(data.status==200){
                               $("#userloginform").after('<p class="error_text text-info text-center">Successfully Logined</p>')
                                 setTimeout(function () {
                                        window.location.href='profile/';
                                 },1000)
                          }
                          if(data.status==404){
                               $("#userloginform").after('<p class="error_text text-danger text-center">'+data.message+'</p>')
                          }
                         $("#userloginform")[0].reset()
                        },3000)
                },
                error:function (data) {
                    console.log('error');

                }
            });
        }
        return false;
    });
});