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
    var width = progress_line / progress;
    elem.style.width = width + '%'
}
// lesson number one
if (points <= 399) {
    progress_bar('onebar', 2) 
}else{
    var elem = document.getElementById('onebar');
    elem.style.width = 100 + '%'
}
// lesson number two
if (points >= 400) {
    progress_bar('twobar', 2) 
}
if (points >= 799) {
    var elem = document.getElementById('twobar');
    elem.style.width = 100 + '%'
}
// lesson number three
if (points >= 800) {
    progress_bar('threebar', 2) 
}
if (points >= 1199) {
    var elem = document.getElementById('threebar');
    elem.style.width = 100 + '%'
}

// lesson number fourbar
if (points >= 1200) {
    progress_bar('fourbar', 2) 
}
if (points >= 1599) {
    var elem = document.getElementById('fourbar');
    elem.style.width = 100 + '%'
}

// lesson number fivebar
if (points >= 1600) {
    progress_bar('fivebar', 2) 
}
if (points >= 1999) {
    var elem = document.getElementById('fivebar');
    elem.style.width = 100 + '%'
}


// lesson number four 
// if (points >= 800) {
// if (points >= 1199) {
    // var elem = document.getElementById('threebar');
    // elem.style.width = 100 + '%'
// }


//=======================================================================

$(window).ready(function() {
    setTimeout("$('.lessonstart').fadeIn('slow');", 200);
})

$('#click-next').click(function() {
    // $('#div_number_one').hide('slow')
    $('#div_number_one').hide()

    document.getElementById("circle2").style.background='green'
    document.getElementById("circle1").style.background='grey'

    setTimeout("$('#div_number_two').fadeIn('slow');", 200);
    // $('#div_number_two').show('slow')
})
$('#click-back').click(function() {
    // $('#div_number_one').show('slow')
    setTimeout("$('#div_number_one').fadeIn('slow');", 200);
    // $('#div_number_two').hide('slow')
    $('#div_number_two').hide()
    document.getElementById("circle1").style.background='green'
    document.getElementById("circle2").style.background='grey'
})

// console.log($('#div_number_one').is(':hidden'))
// console.log($('#div_number_two').is(':hidden'))


// if($('#div_number_one.is'.is(':visible'))) {
// console.log('My name is div_number_one and I am visible')
// }

// if($('#div_number_two'.is(':hidden'))) {
    // console.log('My name is div_number_two and I am visible')
// }