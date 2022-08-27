document.addEventListener('DOMContentLoaded', _ => {
    let referrer = document.referrer;
    let loginPage = window.location.origin + '/login.html';

    if (window.location.search === '?error=login') {
        alert('Logue para poder acessar');
    }

    if (!getCookie('canEnter')) {
        window.location.replace('./login.html?error=login');
    } else {

        // lets make a little bit difficult to make more funny
        fetch('./products.json').then(data => data.json()).then((json) => {

            let tbody = document.getElementById('table-products');

            tbody.innerHTML = '';

            let numberOfRows = randomNumber(4, 10);
            let items = json.items;

            items = shuffleArray(items);

            for (let row = 0; row < numberOfRows; row++) {
                tbody.innerHTML += `<tr>
                <td>${items.shift().capitalize()}</td>
                <td>${randomNumber(2, 50)}</td>
            </tr>`;
            }
        }).catch(_ => {
            alert('Aplicação não conseguiu se conectar ou encontrar o arquivo de produtos. Tente novamente mais tarde.');
        });
    }

    document.querySelector('.btn-logout').addEventListener('click', _ => {
        deleteCookie('canEnter');
        window.location.href = 'login.html';
    });

});