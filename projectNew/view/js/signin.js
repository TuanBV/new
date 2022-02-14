// validate Login
jQuery("#formLogin").validate({
    rules: {
        username: {maxlength: 25}
    },
    messages:{
        username: {
            required: "Please enter username",
            maxlength: "No more than 25 characters"
        },
        password: {
            required: "Please enter password"
        }
    },
    submitFormLogin: function(form){
        form.submit();
    }
});
