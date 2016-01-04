$(document).ready(function () {
    $('#query').click(function (){
        // alert($('#slot_candidate').val());
        // alert($('#t').text());

		$.ajax({
            url: 'http://127.0.0.1:5000/rs/rs_handler/',
            cache: false,
            async: true,
            dataType: 'html',
            type:'POST',
            data: { 'slot_candidate': $('#slot_candidate').val(),'title': $('#title').text(),},
            error: function(xhr) {
                alert('Ajax request ERROR');
            },
            success: function(response) {
                $("body").html(response);
                // alert(response);
            }
        });
    });
});
