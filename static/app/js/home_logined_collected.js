$(function () {
    $('.movie-like').click(function () {
        var heart = $(this);
        var postid = heart.parents('li').attr('postid');

        $.getJSON('/app/addmovie/', {'postid': postid}, function (data) {
                console.log('del');
                window.location.reload();
        })
    })
})