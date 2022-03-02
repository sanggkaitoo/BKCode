$(document).ready(function() {
    var code = $(".code-input")[0];
    var editor = CodeMirror.fromTextArea(code, {
        lineNumbers: true,
        mode: "python"
    });

    $('#language').change(function() {
        editor.setOption("mode", check_mod($(this).val()));
    });

})

function check_mod(id) {
    if(id == '3') {
        return "python";
    } else if (id != "3") {
        return "clike";
    }
}