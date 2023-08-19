$(document).ready(function() {
    // Register button click event
    $("#register-button").click(function() {
        var form = $("#register-form")[0];
        var formData = new FormData(form);
        
        $.ajax({
            type: "POST",
            enctype: "multipart/form-data",
            url: "/register",
            data: formData,
            processData: false,
            contentType: false,
            cache: false,
            success: function(data) {
                $("#register-message").text(data);
            },
            error: function(err) {
                console.log(err);
            }
        });
    });
    
    // Recognize button click event
    $("#recognize-button").click(function() {
        var form = $("#recognize-form")[0];
        var formData = new FormData(form);
        
        $.ajax({
            type: "POST",
            enctype: "multipart/form-data",
            url: "/recognize",
            data: formData,
            processData: false,
            contentType: false,
            cache: false,
            success: function(data) {
                $("#recognize-message").text(data);
            },
            error: function(err) {
                console.log(err);
            }
        });
    });
});
