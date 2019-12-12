/**
 * Disambiguate JS
 */

displayTemplateProcess = function () {

    if (validateStartCurate()) {
        var data = new FormData($("#form_select_template")[0]);
        data.append("role", $("#role").text());
        $.ajax({
            url: disambiguateCurate,
            type: 'POST',
            data: data ,
            dataType: "json",
            contentType: false,
            processData: false,
            success: function (data) {
                if (data.form) {
                    $("#disambiguate-name-modal").modal("show");
                    $("#disambiguate-form").html(data.form);

                } else {
                    call_start_curate('');
                }
            },
            error: function (data) {
                call_start_curate('');
            }
        });

    }
};

start_curate = function () {
    call_start_curate($('input[name=names]:checked', '#disambiguate-form').val());
};

call_start_curate = function (sparqlUrl) {
    // TODO fix the sparqlUrl that sometimes doesn't work.
    var formData = new FormData($( "#form_select_template" )[0]);
    formData.append('sparqlUrl', sparqlUrl);
    $.ajax({
        url: startCurate,
        type: 'POST',
        data: formData,
        cache: false,
        contentType: false,
        processData: false,
        success: function(data) {
            window.location = data;
        },
        error: function(data) {
            // FIXME: temp fix for safari support
            $("#id_file").prop('disabled', false);
            // FIXME: temp fix for chrome support (click twice on start raise an error)
            $("#btn-display-data").prop('disabled', false);
            if (data.responseText != "") {
                $("#form_start_errors").html(data.responseText);
                $("#banner_errors").show(500);
            }
        }
    });
};

$("#btn-disambiguate-name").on("click", start_curate);
