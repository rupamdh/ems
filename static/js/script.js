$(document).ready(function () {
    $('.ac-btn').click(function (e) { 
        e.preventDefault();
        $('.ac-cont').removeClass('open');
        if ($(this).next().hasClass('open')) {
            $(this).next().removeClass('open');
        } else {
            $(this).next().addClass('open');
        }
    });  

});