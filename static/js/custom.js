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
        url: '../static/js/countries.json',
        getValue: 'name',
        list: {
            onChooseEvent: function() {
                var selected = $("#suggestion-search").getSelectedItemData();
                console.log(selected);
            }
        } 
    };
    $('#suggestion-search').easyAutocomplete(options);

});