var $modal = $('#MyModal');
var $link = $('#mylink');
var $close = $(".close");

$link.on('click', function(e) {
    $modal.toggle();
    e.stopPropagation();
});

$close.on('click', function(e) {
    $modal.hide();
    e.stopPropagation();
});

$modal.on('click', function(e) {
    e.stopPropagation();
});

$(document).on('click', function () {
    $modal.hide();
});