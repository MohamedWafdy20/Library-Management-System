document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");

    form.addEventListener("submit", function (event) {

        const passwordFields = document.querySelectorAll(
            'input[type="password"]'
        );

        const password = passwordFields[0].value;
        const confirmPassword = passwordFields[1].value;


        if (password.length < 8) {

            alert("Password must be at least 8 characters");
            event.preventDefault();

        }

        else if (password !== confirmPassword) {

            alert("Passwords do not match");
            event.preventDefault();

        }

    });

});