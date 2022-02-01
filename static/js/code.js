$(document).ready(function() {
    var code = $(".code-input")[0];
    var editor = CodeMirror.fromTextArea(code, {
        lineNumbers: true,
        mode: "python"
    });

    $('#language').change(function() {
        editor.setOption("mode", $(this).val());
    });

})
