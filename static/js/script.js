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

    $('.nav-item.has-child').click(function (e) { 
        //e.preventDefault();
        $(this).find('ul').slideDown();
        $(this).addClass('active')
        
    });

    
    $('#emptable').DataTable({
        "columnDefs": [
            { "orderable": false, "targets": [1, 2, 3] } // Disables sorting for columns 1 and 2
        ]
    });
});