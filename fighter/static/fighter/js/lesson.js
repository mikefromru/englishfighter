var OnclickList = []

function dell_word() {
    var f = myform.field.value.split(" ")
    f.pop()
    myform.field.value = f.join(" ")
    OnclickList.pop()

    var f_format = f.slice(1)
    if (f_format.length == 0) {
        var group = listBtns.slice(0, 10)
        genButtons(group)
        genButtons(listBtns)
    
    }else if(f_format.length == 1) {
        var group = listBtns.slice(10, 20)
        // genButtons(group)
        genButtons(listBtns.slice(10))

    }else if(f_format.length == 2) {
        var group = listBtns.slice(20, 30) 
        genButtons(group)
        genButtons(listBtns)
        // genButtons(listBtns.slice(20, 30))
    }
}
  
// window.addEventListener("DOMContentLoaded", function() {
    var x = 0;
    var br = document.createElement("br");
    function genButtons(a) {
        var parent = document.getElementById('_buttons'),
        inp = parent.querySelectorAll("[id^='b']");
        [].forEach.call(inp, function(btn){
            parent.removeChild(btn)
        });
        a.slice(0, 10).forEach(function(str, x){
            var btn = document.createElement("input");
            btn.id = "b" + x;
            btn.value = str;
            btn.type = "button";
            btn.className = "btns";
            if ((x - 5)%5 == 0) {
                document.getElementById('_buttons').appendChild(br)
            }
            parent.appendChild(btn)

            btn.addEventListener("click", function(){
                genButtons(a.slice(10))
                get_and_post(btn)
                // var valueForm = myform.field.value += ' ' + this.value;
                // var newValueFormFormat = $.trim(valueForm)
                // var text = document.getElementById('_buttons').value

                // var lenVFF = newValueFormFormat.split(' ')
                // var splitEnglish = english.split(' ')

                // // console.log(splitEnglish)
                // // console.log(newValueFormFormat)
                // // console.log(english)

                // if(newValueFormFormat == english) {
                //     alert('good')
                //     $(document).ready(function() {
                //         $.ajax({
                //             url: "",
                //             type: "POST",
                //             data: $("#myform").serialize(),
                //             success: function(html) {
                //                 $("body").html(html)
                //                 $("#myform")[0].reset()
                //                 genButtons(listBtns)
                //             }
                //         })
                //     })

                // }else if(lenVFF.length >= splitEnglish.length) {
                //     alert('no')
                //     $(document).ready(function() {
                //         $.ajax({
                //             url: "",
                //             type: "GET",
                //             data: $("#myform").serialize(),
                //             success: function(html) {
                //                 $("body").html(html)
                //                 $("#myform")[0].reset()
                //                 genButtons(listBtns)
                //             }
                //         })
                //     })
                // }
            })
        })
    }
genButtons(listBtns)
// })

function get_and_post(btn) {
    var valueForm = myform.field.value += ' ' + btn.value;
    var newValueFormFormat = $.trim(valueForm)
    var text = document.getElementById('_buttons').value

    var lenVFF = newValueFormFormat.split(' ')
    var splitEnglish = english.split(' ')

    // console.log(splitEnglish)
    // console.log(newValueFormFormat)
    // console.log(english)

    if(newValueFormFormat == english) {
        alert('good')
        $(document).ready(function() {
            $.ajax({
                url: "",
                type: "POST",
                data: $("#myform").serialize(),
                success: function(html) {
                    $("body").html(html)
                    $("#myform")[0].reset()
                    genButtons(listBtns)
                }
            })
        })

    }else if(lenVFF.length >= splitEnglish.length) {
        alert('no')
        $(document).ready(function() {
            $.ajax({
                url: "",
                type: "GET",
                data: $("#myform").serialize(),
                success: function(html) {
                    $("body").html(html)
                    $("#myform")[0].reset()
                    genButtons(listBtns)
                }
            })
        })
    }
}