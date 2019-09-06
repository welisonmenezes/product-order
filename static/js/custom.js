$(window).on('load', function() {

    $('.file-upload-browse').on('click', function() {
        var t = $(this);
        t.parent().parent().parent().find('.file-upload-default').click();
    });

    $('.file-upload-default').on('change', function(e) {
        var t = $(this);
        t.parent().find('.file-upload-info').val(t.val());
    });

});