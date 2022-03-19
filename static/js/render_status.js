$(document).ready(function() {
    if ($('#status').text() == '200') {
        $('#status').text('OK')
    } else if ($('#status').text() == '201') {
        $('#status').text('Accepted')
    } else if ($('#status').text() == '400') {
        $('#status').text('Wrong Answer')
    } else if ($('#status').text() == '401') {
        $('#status').text('Compilation Error')
    } else if ($('#status').text() == '402') {
        $('#status').text('Runtime Error')
    } else if ($('#status').text() == '403') {
        $('#status').text('Invalid File')
    } else if ($('#status').text() == '404') {
        $('#status').text('File Not Found')
    } else if ($('#status').text() == '408') {
        $('#status').text('Time Limit Exceeded')
    }
})