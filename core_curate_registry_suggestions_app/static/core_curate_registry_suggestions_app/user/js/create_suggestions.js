/**
 * Create suggestions
 */

$(document).ready(function () {
    $.ajax({
        url: getSuggestions,
        data: {'id': curateDataStructureId},
        type: 'POST',
        dataType: "json",
        success: function (data) {
            if (data.abstract != "") {
                var textarea = $("li:contains('Description')").find("textarea");
                textarea.val(data.abstract);
                textarea.blur()
            }
            if (data.homepage != "") {
                var url = $("input[placeholder='Enter a web site URL']");
                url.val(data.homepage);
                url.blur();
            }
            if (data.label != "") {
                // TODO create alternative name ?
                $("input[placeholder='Enter your Resource\\'s name (ex. Materials Data Curation System)']").val(data.label);
                $("input[placeholder='Enter your Resource\\'s name (ex. Materials Data Curation System)']").blur();
            }
        },
        error: function (data) {
        }
    });
});