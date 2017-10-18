/*REVIEWS JAVASCRIPT FILE*/

$(document).ready(function(){
    $("div[name='Ad']").click(function(){
        $(this).hide();
    });
});

$(document).ready(function(){
    var count = 1;
    $("button").click(function(){
        $("#counter").text(count++);
    });
});