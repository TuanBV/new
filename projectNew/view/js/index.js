// button active
// var btnMenu = document.querySelectorAll("a");
// btnMenu.forEach((li) => {
//   li.addEventListener("click", function () {
//     li.classList.add("active");
//   });
// });
// validate form change password using jquery
jQuery("#formChangePw").validate({
  rules: {
    passwordnow: { required: true, minlength: 8 },
    passwordnew: { minlength: 8, maxlength: 30 },
    repasswordnew: { minlength: 8, maxlength: 30, equalTo: "#passwordnew" },
  },
  messages: {
    passwordnow: {
      required: "Please enter your password now",
      minlength: "Please at least 8 characters",
    },
    passwordnew: {
      required: "Please enter your password new",
      minlength: "Please at least 8 characters",
      maxlength: "Please enter no more than 30 characters",
    },
    repasswordnew: {
      required: "Please enter your password new",
      minlength: "Please at least 8 characters",
      maxlength: "Please enter no more than 30 characters",
      equalTo: "Confirm password new error !",
    },
  },
  submitHandler: function (form) {
    form.oninput();
  },
});
// validate reset password
$("#resetPw").validate({
  rules: {
    passwordnew: { minlength: 8, maxlength: 30 },
    repasswordnew: { minlength: 8, maxlength: 30, equalTo: "#passwordnew" },
  },
  messages: {
    passwordnew: {
      required: "Please enter your password new",
      minlength: "Please  at least 8 characters",
      maxlength: "Please enter no more than 30 characters",
    },
    repasswordnew: {
      required: "Please enter your password new",
      minlength: "Please  at least 8 characters",
      maxlength: "Please enter no more than 30 characters",
      equalTo: "Confirm password new error !",
    },
  },
  submitFormResetPassword: function (form) {
    form.oninput();
  },
});

// dateITA method
$.validator.addMethod(
  "dateITA",
  function (value, elemnet) {
    var check = false;
    var re = /^\d{4}\/\d{1,2}\/\d{1,2}$/;
    var adata, gg, mm, aaaa, xdata;

    adata = value.split("-");
    gg = parseInt(adata[2], 10);
    mm = parseInt(adata[1], 10);
    aaaa = parseInt(adata[0], 10);
    xdata = new Date(aaaa, mm - 1, gg, 12, 0, 0, 0);
    if (
      xdata.getUTCFullYear() === aaaa &&
      xdata.getUTCFullYear() > 1950 &&
      xdata.getUTCMonth() === mm - 1 &&
      xdata.getUTCDate() === gg
    ) {
      check = true;
    } else {
      check = false;
    }
    return check;
  },
  "Please enter a format"
);
// jquery add method greater than date
$.validator.addMethod(
  "greaterThan",
  function (value, element, params) {
    var dateStart = $("#timeRateStart").val();
    var dateEnd = $("#timeRateEnd").val();
    return dateEnd > dateStart;
  },
  "Please confirm choose time rate!!!."
);
// birthday user
$.validator.addMethod(
  "greaterThan1",
  function (value, element, params) {
    var birthday = document.getElementById("birthday").value;
    const d = new Date().toISOString().split("T");
    return birthday < d[0];
  },
  "Please choose birhtday"
);
// validate form  create user using jquery
$("#formCreateUser").validate({
  rules: {
    fullname: { maxlength: 100 },
    username: { minlength: 4, maxlength: 30 },
    email: { email: true, maxlength: 100 },
    rdoPosition: { required: true },
    birthday: { greaterThan1: ["#birthday", new Date()] },
    address: { maxlength: 200 },
  },
  messages: {
    fullname: {
      maxlength: "Please enter max 100 characters",
    },
    username: {
      required: "Please enter Username",
      minlength: "Please  at least 4 characters",
      maxlength: "Max 30 characters",
    },
    email: {
      email: "Please enter format email",
      required: "Please confirm email",
    },
    rdoPosition: {
      required: "Please choose position for account",
    },
    birthday: {},
    address: {
      maxlength: "Please enter no more than 200 characters",
    },
  },
});
// validate form create time rate using jquery
$("#formTimeRate").validate({
  rules: {
    nameTime: { maxlength: 200 },
    timeRateEnd: { greaterThan: ["#timeRateEnd", "#timeRateStart"] },
  },
  messages: {
    nameTime: {
      required: "Please enter name time rate",
      maxlength: "Please enter no more than 200 characters",
    },
    timeRateStart: {
      required: "You choose time start !",
      dateITA: true,
    },
    timeRateEnd: {
      required: "You choose time end !",
      dateITA: true,
    },
  },
});
//  validate form edit time rate
$("#formEditTimeRate").validate({
  rules: {
    nameTime: { maxlength: 100 },
    timeRateStart: { greaterThan: ["#timeRateEnd", "#timeRateStart"] },
    timeRateEnd: { greaterThan: ["#timeRateEnd", "#timeRateStart"] },
  },
  messages: {
    nameTime: {
      required: "Please enter name time rate",
      maxlength: "Please enter no more than 100 characters",
    },
    timeRateStart: {
      required: "You choose time start !",
      dateITA: true,
      greaterThan: "Please confirm choose time rate!!!",
    },
    timeRateEnd: {
      required: "You choose time end !",
      dateITA: true,
    },
  },
});
// menu 
$(document).ready(function () {
  const obj = JSON.parse(localStorage.getItem('user'));
  const cookie = document.cookie.split("=");
  if (obj == null ){
    location.href = "/view/sign-in.html";
  }
  $("#logout").click(function () {
    deleteCookie(cookie[1]);
    localStorage.clear();
    location.href = "/view/sign-in.html";
  });
  menu();
  // button back
  window.addEventListener("pageshow", function (event) {
    var historyTraversal =
      event.persisted ||
      (typeof window.performance != "undefined" &&
        window.performance.navigation.type === 2);
    if (historyTraversal) {
      window.location.reload();
    }
  });
});
// menubar();
function menu(){
  const obj = JSON.parse(localStorage.getItem('user'));
  if (obj[0].idposition == 1) {
    $(".admin").show();
    $(".manager").hide();
  } else if (obj[0].idposition == 2) {
    $(".admin").hide();
    $(".manager").show();
  } else {
    $(".admin").hide();
    $(".manager").hide();
  }
}
// delete Cookie
function deleteCookie(cname) {
  document.cookie =
    "username" + "=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;";
}
