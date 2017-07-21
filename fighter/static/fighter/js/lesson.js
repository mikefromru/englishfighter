var OnclickList = []

function dell_word() {
    var f = myform.field.value.split(" ")
    f.pop()
    myform.field.value = f.join(" ")
    OnclickList.pop()

    var f_format = f.slice(1)
    if (f_format.length == 0) {
        console.log('ZERO')
        var group = listBtns.slice(0, 10)
        genButtons(group)
        genButtons(listBtns)
    
    }else if(f_format.length == 1) {
        console.log('ONE')
        var group = listBtns.slice(10, 20)
        genButtons(listBtns.slice(10))

    }else if(f_format.length == 2) {
        console.log('TWO')
        var group = listBtns.slice(20, 30) 
        genButtons(group)
        genButtons(listBtns.slice(20))

    }else if(f_format.length == 3) {
        console.log('THREE')
        var group = listBtns.slice(30, 40) 
        genButtons(listBtns.slice(30))
        
    }else if(f_format.length == 4) {
        console.log('FOUR')
        var group = listBtns.slice(40, 50) 
        genButtons(group)
        genButtons(listBtns.slice(40))

    }else if(f_format.length == 5) {
        console.log('FIVE')
        var group = listBtns.slice(50, 60) 
        genButtons(group)
        genButtons(listBtns.slice(50))

    }else if(f_format.length == 6) {
        console.log('SIX')
        var group = listBtns.slice(60, 70) 
        genButtons(group)
        genButtons(listBtns.slice(60))
    }
}

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
            })
        })
    }
genButtons(listBtns)

function get_and_post(btn) {
    var valueForm = myform.field.value += ' ' + btn.value;

    var newValueFormFormat = $.trim(valueForm)
    var text = document.getElementById('_buttons').value

    var lenVFF = newValueFormFormat.split(' ')
    var splitEnglish = english.split(' ')

    console.log(splitEnglish.length, 'splitEnglish')
    console.log(lenVFF.length, 'lenVFF')

    if(newValueFormFormat == english) {
        $(document).ready(function() {
            $.ajax({
                url: "",
                type: "POST",
                data: $("#myform").serialize(),
                success: function(html) {
                alert('good')
                    $("body").html(html)
                    $("#myform")[0].reset()
                    genButtons(listBtns)
                }
            })
        })

    }else if(lenVFF.length >= splitEnglish.length) {
        $(document).ready(function() {
            $.ajax({
                url: "",
                type: "GET",
                data: $("#myform").serialize(),
                success: function(html) {
                    alert('no')
                    $("body").html(html)
                    genButtons(listBtns)
                    $("#myform")[0].reset()
                }
            })
        })
    }
}