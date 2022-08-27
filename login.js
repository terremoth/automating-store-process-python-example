/**
 * This code is for webdriver simulation purposes only! Never EVER do these things in your life!
 * Do not EVER put sensitive information in your front-end files!
 */
document.addEventListener('DOMContentLoaded', _ => {

    if (window.location.search === '?error=login') {
        alert('Logue para poder acessar o sistema!');
    }

    if (getCookie('canEnter')) {
        window.location.replace('./admin.html');
    }

    document.getElementById('form-login').addEventListener('submit', ev => {

        ev.preventDefault();

        let email = document.getElementById('email').value;
        let password = document.getElementById('password').value;

        if (email === 'admin@admin' && password === 'admin') {
            setCookie('canEnter', 1, 1);
            window.location.replace('./admin.html');
        } else {
            let myModal = new bootstrap.Modal(document.getElementById('modal-error'))
            myModal.toggle()
        }

    });
});