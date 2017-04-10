$(document).ready(function(){

    $("#loginform").validate({

       rules:{

            username:{
                required: true,
                minlength: 4,
                maxlength: 16,
            },

            password:{
                required: true,
                minlength: 6,
                maxlength: 16,
            },
       },

       messages:{

            username:{
                required: "Это поле обязательно для заполнения",
                minlength: "Логин должен быть минимум 4 символа",
                maxlength: "Максимальное число символо - 16",
            },

            password:{
                required: "Это поле обязательно для заполнения",
                minlength: "Пароль должен быть минимум 6 символа",
                maxlength: "Пароль должен быть максимум 16 символов",
            },

       }

    });

});