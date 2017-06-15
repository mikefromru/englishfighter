window.addEventListener("DOMContentLoaded", function() {
    var x = 0;
    var br = document.createElement("br");
    function genButtons(a) {
    
        // var listBtns = "{{ stack.buttons }}".split(' ')
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
                // document.getElementById('_buttons').appendChild(btn)
                document.getElementById('_buttons').appendChild(br)
            }
            parent.appendChild(btn)

            btn.addEventListener("click", function(){
                genButtons(a.slice(10))
                var valueForm = myform.field.value += ' ' + this.value;
                var newValueFormFormat = $.trim(valueForm)
                var text = document.getElementById('_buttons').value
                // var english = "{{ stack.english }}"
                // var russia = "{{ stack.russia }}".split(' ')

                var lenVFF = newValueFormFormat.split(' ')
                var splitEnglish = english.split(' ')

                // console.log(splitEnglish)
                // console.log(newValueFormFormat)
                // console.log(english)

                if(newValueFormFormat  == english) {
                    alert('good')
                    $(document).ready(function() {
                        $.ajax({
                            url: "",
                            type: "POST",
                            data: $("#myform").serialize(),
                            success: function(html) {
                                $("body").html(html)
                                $("#myform")[0].reset()
                                // location.reload()
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
                                // location.reload()
                                genButtons(listBtns)
                            }
                        })
                    })
                }


            })
        })
    }
// var something = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
// var listBtns = "{{ stack.buttons }}".split(' ')
genButtons(listBtns)
})