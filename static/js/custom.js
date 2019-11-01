$(window).on('load', function () {
    // NICE UPLOAD FILE
    // trigger click event
    $('.file-upload-browse').on('click', function () {
        var t = $(this);
        t.parent().parent().parent().find('.file-upload-default').click();
    });
    // show selected filename
    $('.file-upload-default').on('change', function (e) {
        var t = $(this);
        t.parent().find('.file-upload-info').val(t.val());
    });


    // INPUT MASKS
    $('.phone').mask('00 0000-00009', { clearIfNotMatch: true, placeholder: '00 0000-00000' });
    $('.money').mask('9999999999.00', { clearIfNotMatch: true, reverse: true, placeholder: '0.0' });
    $('.cep').mask('00000-000', { clearIfNotMatch: true, placeholder: '00000-000' });

    (function ($) {
        'use strict';
        $(function () {
            $('[data-toggle="offcanvas"]').on("click", function () {
                $('.sidebar-offcanvas').toggleClass('active')
            });
        });
    })(jQuery);

});