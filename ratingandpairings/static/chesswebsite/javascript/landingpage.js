document.querySelector('.login-form').addEventListener('submit', function(event) {
    event.preventDefault();

    var username = document.querySelector('[name="username"]').value;
    var password = document.querySelector('[name="password"]').value;

    if (username !== 'correctUsername' || password !== 'correctPassword') {
        var errorMsg = document.getElementById('error-msg');
        errorMsg.textContent = 'Invalid username or password.';
        errorMsg.style.display = 'block';
    } else {
        this.submit();
    }
});
