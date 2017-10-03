var OnclickList = []

function dell_word() {

    var f = myform.field.value.split(" ")

    f.forEach(function(elem, index, arr) {
        if (f[index] == 'a' && f[index + 1] == 'little') {  
            f[index] = f[index].toString() + 'little';
            arr.splice(index + 1, 1)
        }
    })

    f.forEach(function(elem, index, arr) {
        if (f[index] == 'a' && f[index + 1] == 'few') {  
            f[index] = f[index].toString() + 'few';
            arr.splice(index + 1, 1)
        }
    })

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
        genButtons(listBtns.slice(10))

    }else if(f_format.length == 2) {
        var group = listBtns.slice(20, 30) 
        genButtons(group)
        genButtons(listBtns.slice(20))

    }else if(f_format.length == 3) {
        var group = listBtns.slice(30, 40) 
        genButtons(listBtns.slice(30))
        
    }else if(f_format.length == 4) {
        var group = listBtns.slice(40, 50) 
        genButtons(group)
        genButtons(listBtns.slice(40))

    }else if(f_format.length == 5) {
        var group = listBtns.slice(50, 60) 
        genButtons(group)
        genButtons(listBtns.slice(50))

    }else if(f_format.length == 6) {
        var group = listBtns.slice(60, 70) 
        genButtons(group)
        genButtons(listBtns.slice(60))

    }else if(f_format.length == 7) {
        var group = listBtns.slice(70, 80) 
        genButtons(group)
        genButtons(listBtns.slice(70))

    }else if(f_format.length == 8) {
        var group = listBtns.slice(80, 90) 
        genButtons(group)
        genButtons(listBtns.slice(80))

    }else if(f_format.length == 9) {
        var group = listBtns.slice(90, 100) 
        genButtons(group)
        genButtons(listBtns.slice(90))
    }else if(f_format.length == 10) {
        var group = listBtns.slice(100, 110) 
        genButtons(group)
        genButtons(listBtns.slice(100))
    }else if(f_format.length == 11) {
        var group = listBtns.slice(110, 120) 
        genButtons(group)
        genButtons(listBtns.slice(110))
    }else if(f_format.length == 12) {
        var group = listBtns.slice(120, 130) 
        genButtons(group)
        genButtons(listBtns.slice(120))
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
    
    // var lenVFF = newValueFormFormat.split(' ')




/////////////////////////////////////////////////////////


    var tmpEnglish = english.split(' ')

    tmpEnglish.forEach(function(elem, index, arr) {
        if (tmpEnglish[index] == 'a' && tmpEnglish[index + 1] == 'little') {  
            tmpEnglish[index] = tmpEnglish[index].toString() + 'little';
            arr.splice(index + 1, 1)
        }
    })

    tmpEnglish.forEach(function(elem, index, arr) {
        if (tmpEnglish[index] == 'a' && tmpEnglish[index + 1] == 'few') {  
            tmpEnglish[index] = tmpEnglish[index].toString() + 'few';
            arr.splice(index + 1, 1)
        }
    })

    var fresh_newValueFormFormat = newValueFormFormat.split(' ')

    fresh_newValueFormFormat.forEach(function(elem, index, arr) {
        if (fresh_newValueFormFormat[index] == 'a' && fresh_newValueFormFormat[index + 1] == 'little') {  
            fresh_newValueFormFormat[index] = fresh_newValueFormFormat[index].toString() + 'little';
            arr.splice(index + 1, 1)
        }
    })

    fresh_newValueFormFormat.forEach(function(elem, index, arr) {
        if (fresh_newValueFormFormat[index] == 'a' && fresh_newValueFormFormat[index + 1] == 'few') {  
            fresh_newValueFormFormat[index] = fresh_newValueFormFormat[index].toString() + 'few';
            arr.splice(index + 1, 1)
        }
    })



    console.log(tmpEnglish)
    console.log(fresh_newValueFormFormat)

    var newTmpEnglish = tmpEnglish.join(' ')
    var string_fresh_newValueFormat = fresh_newValueFormFormat.join(' ')
    // console.log(newTmpEnglish)
    // console.log(string_fresh_newValueFormat)

    var lenVFF = fresh_newValueFormFormat
    //////////////////////////////////////////////////////////////////////////
    var splitEnglish = english.split(' ')
    // console.log(lenVFF.length, 'this lenVFF')
    // console.log(splitEnglish.length, "this splitEnglish")

    // if(newValueFormFormat.toLowerCase() == english.toLowerCase()) {
    if(string_fresh_newValueFormat.toLowerCase() == newTmpEnglish.toLowerCase()) {
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

    // }else if(lenVFF.length >= splitEnglish.length) {
    }else if(lenVFF.length >= tmpEnglish.length) {
        $(document).ready(function() {
            $.ajax({
                url: "",
                type: "GET",
                data: $("#myform").serialize(),
                success: function(html) {
                    alert("It's not correct\n" + english)
                    $("body").html(html)
                    genButtons(listBtns)
                    $("#myform")[0].reset()
                }
            })
        })
    }
}