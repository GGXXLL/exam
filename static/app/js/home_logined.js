$(function () {
    $('.movie-like').click(function () {
        var heart = $(this);
        var postid = heart.attr('postid');
        // console.log('dianlelelel')
        $.getJSON('/app/addmovie/', {'postid': postid}, function (data) {
            if(data['status']=='200'){
                // console.log('add');
                heart.css('color', 'red');
            }
            else {
                // console.log('del');
                heart.css('color', 'black');
            }
        })
    })
})