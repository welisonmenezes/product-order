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

        $('#error-msg').html('');
    });


    // CALULATE THE VALUE BY AMOUNT
    $('#p-qtd').on('input', function () {
        var t = $(this);
        var prod_val = $('#p-valor').val();

        if (prod_val !== '' && !isNaN(t.val())) {
            var valor = parseFloat(prod_val) * parseFloat(t.val());
            $('#p-val').val(valor.toFixed(2));
        }
    });


    // ADD THE PRODUCT
    $('#add-product').on('click', function () {
        var product_id = $('#p-id').val();

        if (product_id !== '') {
            var order_id = $('#order_id').val();
            if (order_id !== '') {
                addProductToBackend();
            } else {
                addOrderToBackend();
            }
        } else {
            $('#error-msg').html('Selecione um produto para adicionar ao pedido');
        }

    });


    // ADD THE ORDER TO DATABASE
    function addOrderToBackend() {
        $('.actions').addClass('none');
        $('.loader').removeClass('none');
        
        $.ajax({
            method: 'POST',
            url: '/order/add-order',
            data: { client: $('#cliente').val(), obs: $('#observacao').val() }
        }).done(function (data) {
            if (data && data.order_id) {
                $('#order_id').val(data.order_id);
                addProductToBackend();
            } else {
                $('#error-msg').html(data.message);
            }

            $('.actions').removeClass('none');
            $('.loader').addClass('none');
        });
    }


    // ADD THE PRODUCT TO ORDER
    function addProductToBackend() {
        $('.actions').addClass('none');
        $('.loader').removeClass('none');

        $.ajax({
            method: 'POST',
            url: '/order/add-product-order',
            data: {
                pedidos_id: $('#order_id').val(),
                produtos_id: $('#p-id').val(),
                quantidade: $('#p-qtd').val(),
                valor: $('#p-val').val(),
                observacao: $('#p-desc').val()
            }
        }).done(function (data) {
            if (data && data.pedidos_id) {
                addProductToFrontend();
            } else {
                $('#error-msg').html(data.message);
            }

            $('.actions').removeClass('none');
            $('.loader').addClass('none');
        });
    }


    // ADD THE REGISTERED PRODUCT TO FRONTEND
    function addProductToFrontend() {
        var row = $('<tr>');

        var td_img = $('<td><img src="data:image/png;base64,' + $('#p-imagem').val() + '" /></td>');
        row.append(td_img);

        var td_id = $('<td class="row-id">' + $('#p-id').val() + '</td>');
        row.append(td_id);

        var td_desc = $('<td>' + $('#p-descricao').val() + '</td>');
        row.append(td_desc);

        var td_val_u = $('<td class="row-value">' + $('#p-valor').val() + '</td>');
        row.append(td_val_u);

        var td_qtd = $('<td><input type="number" class="form-control edit-qtd-field qtd-field" value="' + $('#p-qtd').val() + '" /></td>');
        row.append(td_qtd);

        var td_val = $('<td class="row-total">' + $('#p-val').val() + '</td>');
        row.append(td_val);

        var td_obs = $('<td><input type="text" class="form-control obs-field" value="' + $('#p-desc').val() + '" /></td>');
        row.append(td_obs);

        var td_edit = $('<td><button type="button" class="btn btn-primary p-edit">Editar</button> <button type="button" class="btn btn-danger p-delete">Deletar</button></td>');
        row.append(td_edit);

        $('#p-body').append(row);
        $('#p-has').removeClass('none');
        $('#p-not-has').addClass('none');
        $('#modalProduto').modal('toggle');
    }


    // TRIGGER THE DELETE PRODUCT FORM ORDER ACTIONS
    $('body').on('click', '.p-delete', function() {
        var t = $(this);
        var row = t.parent().parent();
        var order_id = $('#order_id').val();
        var product_id = row.find('.row-id').text();

        deleteProductFromOrder(order_id, product_id, row);
    });


    // DELETE PRODUCT ORDER FROM SERVER
    function deleteProductFromOrder(order_id, product_id, row) {
        $.ajax({
            method: 'POST',
            url: '/order/delete-product-order',
            data: { order_id: order_id, product_id: product_id, from: $('#page-origin').val() }
        }).done(function (data) {
            if (data && data.message) {
                $('#textModalMessage').html(data.message);
                deleteFrontendProductFromOrder(row);
            } else {
                $('#textModalMessage').html('Desculpe, ocorreu um problema ao deletar este item.');
            }
            $('#modalMessage').modal('toggle');
        });
    }


    // DELETE PRODUCT ORDER FROM FRONTEND
    function deleteFrontendProductFromOrder(row) {
        row.remove();
        if ($('#p-body').find('tr').length < 1) {
            $('#p-has').addClass('none');
            $('#p-not-has').removeClass('none');
            $('#order_id').val('');
        }
    }



    $('body').on('input', '.edit-qtd-field', function() {
        var t = $(this);
        var newQtd = t.val();
        var row = t.parent().parent();
        var f_total = row.find('.row-total');
        var f_value = row.find('.row-value');
        var value = parseFloat(f_value.text()).toFixed(2);

        if (isNaN(newQtd) || newQtd < 1) {
            t.val('1');
            newQtd = 1;
        }

        var newTotal = value * newQtd;
        f_total.html(newTotal.toFixed(2));
    });



    // TRIGGER THE EDIT PRODUCT FORM ORDER ACTIONS
    $('body').on('click', '.p-edit', function() {
        var t = $(this);
        var row = t.parent().parent();
        var order_id = $('#order_id').val();
        var product_id = row.find('.row-id').text();
        var qtd = row.find('.qtd-field').val();
        var obs = row.find('.obs-field').val();
        var total = row.find('.row-total').text();

        editProductFromOrder(order_id, product_id, qtd, obs, total);
    });


    function editProductFromOrder(order_id, product_id, qtd, obs, total) {
        $.ajax({
            method: 'POST',
            url: '/order/edit-product-order',
            data: { order_id: order_id, product_id: product_id, quantidade: qtd, observacao: obs, valor: total }
        }).done(function (data) {
            if (data && data.message) {
                $('#textModalMessage').html(data.message);
            } else {
                $('#textModalMessage').html('Desculpe, ocorreu um problema ao editar este item.');
            }
            $('#modalMessage').modal('toggle');
        });
    }


});