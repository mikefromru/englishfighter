var $id_about = document.getElementById("_about")
    // var bar = "{{user.userprofile.about}}"
    var arr = bar.split(" ")
    var text = ""
    var start = 0
    var end = 10
    while(arr.length > 0) {
        var elem5 = arr.splice(start, end)
        text += elem5.join(" ") + "<br />"
    }
    $id_about.innerHTML = text 
