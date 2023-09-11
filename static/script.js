$(document).ready(function() {
    $("#register-button").click(function() {
        var name = $("#name-input").val();
        var formData = new FormData($("#register-form")[0]);

        $.ajax({
            url: "/register",
            type: "POST",
            data: formData,
            contentType: false,
            processData: false,
            success: function(response) {
                $("#register-message").text(response);
            },
            error: function(error) {
                $("#register-message").text("An error occurred during registration.");
            }
        });
    });

    $("#recognize-button").click(function() {
        var formData = new FormData($("#recognize-form")[0]);

        $.ajax({
            url: "/recognize",
            type: "POST",
            data: formData,
            contentType: false,
            processData: false,
            success: function(response) {
                $("#recognize-message").text(response);
            },
            error: function(error) {
                $("#recognize-message").text("An error occurred during recognition.");
            }
        });
    });
});
