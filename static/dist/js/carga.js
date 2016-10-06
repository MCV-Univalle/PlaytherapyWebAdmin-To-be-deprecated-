$(window).on('load', function() {
    $("#full-screen").hide();
    $("#main-content").show();
    $("#myfooter").show();
    $("#header-content").show("fast");
});


function disableItem(itemID){
    $(''+itemID).prop("disabled", true);
}

function enableItem(itemID){
    $(''+itemID).prop("disabled", false);
}