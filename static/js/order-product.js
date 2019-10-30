$(window).on('load', function () {

    // SUGGESTION FIELD
    var options = {
        url: function (phrase) {
            return '/product/search-prod/' + phrase;
        },
        getValue: 'descricao',
        list: {
            onChooseEvent: function () {
                var selected = $("#suggestion-search").getSelectedItemData();
                $('#p-img').attr('src', 'data:image/png;base64,' + selected.imagem);

                if ($('#p-qtd').val() !== '' && !isNaN($('#p-qtd').val())) {
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


    // CLOSE MODAL EVENT
    $('#modalProduto').on('hidden.bs.modal', function (e) {
        $('#suggestion-search').val('');
        $('#p-qtd').val('1');
        $('#p-val').val('');
        $('#p-desc').val('');
        $('#p-img').attr('src', '');

        $('#p-id').val('');
        $('#p-descricao').val('');
        $('#p-imagem').val('');
        $('#p-valor').val('');
    });


    // CALULATE THE VALUE BY AMOUNT
    $('#p-qtd').on('input', function() {
        var t = $(this);
        var prod_val = $('#p-valor').val();

        if (prod_val !== '' && ! isNaN(t.val())) {
            var valor = parseFloat(prod_val) * parseFloat(t.val());
            $('#p-val').val(valor.toFixed(2));
        }
    });


    // ADD THE PRODUCT
    $('#add-product').on('click', function() {

        var row = $('<tr>');

        var td_img = $('<td><img src="data:image/png;base64,' + $('#p-imagem').val() + '" /></td>');
        row.append(td_img);

        var td_id = $('<td class="row-id">' + $('#p-id').val() + '</td>');
        row.append(td_id);

        var td_desc = $('<td>' + $('#p-descricao').val() + '</td>');
        row.append(td_desc);

        var td_val_u = $('<td>' + $('#p-valor').val() + '</td>');
        row.append(td_val_u);

        var td_qtd = $('<td><input type="text" class="form-control" value="' + $('#p-qtd').val() + '" /></td>');
        row.append(td_qtd);

        var td_val = $('<td>' + $('#p-val').val() + '</td>');
        row.append(td_val);

        var td_obs = $('<td><input type="text" class="form-control" value="' + $('#p-desc').val() + '" /></td>');
        row.append(td_obs);

        var td_edit = $('<td><button type="button" class="btn btn-primary p-edit">Deletar</button> <button type="button" class="btn btn-danger p-delete">Deletar</button></td>');
        row.append(td_edit);

        $('#p-body').append(row)

        $('#p-has').removeClass('none');
        $('#p-not-has').addClass('none');
        $('#modalProduto').modal('toggle');
    });

});