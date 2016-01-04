$(document).ready(function () {
    $('#query').click(function (){
        // alert($('#slot_candidate').val());
        // alert($('#t').text());
        // alert(base_url+'/rs/rs_handler/');
        $.ajax({
            // url: base_url+'/rs/rs_handler/',
            url: '/rs/rs_handler/',
            crossDomain: true,
            dataType: 'html',
            type:'POST',
            data: { 'slot_candidate': $('#slot_candidate').val(),'title': $('#title').text(),},
            error: function(xhr) {
                alert('Ajax request ERROR:'+base_url+'/rs/rs_handler/');
            },
            success: function(response) {
                $("body").html(response);
                // alert(response);
            }
        });
    })
});
