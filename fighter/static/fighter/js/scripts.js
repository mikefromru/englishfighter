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

//############ PROGRESS BAR ###############
function progress_bar(bar, progress) {
    var elem = document.getElementById(bar);
    var width = progress_line / 2;
    // var width = 190 / 2;
    console.log(width)
    elem.style.width = width + '%'
}

progress_bar('onebar')
// progress_bar('onebar', progress)