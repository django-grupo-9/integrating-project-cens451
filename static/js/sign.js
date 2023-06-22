function togglePasswordVisibility() {
    var passwordInput = document.getElementById("password");
    var showPasswordBtn = document.getElementById("showPasswordBtn");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
    } else {
        passwordInput.type = "password";
    }
}

function togglePassword1Visibility() {
    var passwordInput = document.getElementById("password1");
    var showPasswordBtn = document.getElementById("showPasswordBtn1");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
    } else {
        passwordInput.type = "password";
    }
}

function togglePassword2Visibility() {
    var passwordInput = document.getElementById("pass");
    var showPasswordBtn = document.getElementById("showPasswordBtn2");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
    } else {
        passwordInput.type = "password";
    }
}