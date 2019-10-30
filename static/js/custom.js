$(window).on('load', function() {


    // NICE UPLOAD FILE
    // trigger click event
    $('.file-upload-browse').on('click', function() {
        var t = $(this);
        t.parent().parent().parent().find('.file-upload-default').click();
    });
    // show selected filename
    $('.file-upload-default').on('change', function(e) {
        var t = $(this);
        t.parent().find('.file-upload-info').val(t.val());
    });


    // SUGGESTION FIELD
    var options = {
        url: function(phrase) {
            return '/product/search-prod/'+phrase;
        },
        getValue: 'descricao',
        list: {
            onChooseEvent: function() {
                var selected = $("#suggestion-search").getSelectedItemData();
                $('#p-img').attr('src', 'data:image/png;base64,' + selected.imagem);

                if ($('#p-qtd').val() !== '' && ! isNaN($('#p-qtd').val())) {
                    var valor = parseFloat(selected.valor) * parseFloat($('#p-qtd').val());
                    $('#p-val').val(valor.toFixed(2));
                }

                $('#p-id').val(selected.id);
                $('#p-descricao').val(selected.descricao);
                $('#p-valor').val(selected.valor);
                $('#p-imagem').val(selected.imagem);
            }
        } 
    };
    $('#suggestion-search').easyAutocomplete(options);


    $('.phone').mask('00 0000-00009', {clearIfNotMatch: true, placeholder: '00 0000-00000'});
    $('.money').mask('9999999999.00', {clearIfNotMatch: true, reverse: true, placeholder: '0.0'});
    $('.cep').mask('00000-000', {clearIfNotMatch: true, placeholder: '00000-000'});

});