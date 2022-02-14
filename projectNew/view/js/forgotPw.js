// Validate form forgot password
$("#resetPw").validate({
  rules: {
    passwordnew: { minlength: 8, maxlength: 30 },
    repasswordnew: { minlength: 8, maxlength: 30, equalTo: "#passwordnew" }
  },
  messages: {
    passwordnew: {
      required: "Please enter your password new",
      minlength: "Please at least 8 characters",
      maxlength: "Please enter no more than 30 characters"
    },
    repasswordnew: {
      required: "Please enter your password new",
      minlength: "Please at least 8 characters",
      maxlength: "Please enter no more than 30 characters",
      equalTo: "Confirm password new error !"
    }
  },
  submitHandler: function (form) {
    form.oninput();
  }
});