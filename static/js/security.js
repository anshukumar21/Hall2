function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

function buildList() {
    var wrapper = document.getElementById('prism');
    wrapper.innerHTML = "";
    var url = 'https://digi-campus.herokuapp.com/api/security/student-list/';
    fetch(url)
        .then((resp) => resp.json())
        .then(function(data) {
            var list = data;
            for (var i in list) {
                if (list[i].in_hall == true) wrapper.innerHTML += '<tr><td>' + {{ user.profile.first_name } } + ' ' + {
                    { user.profile.last_name } } + '</td><td>E152</td><td>200069</td><td>1111222233</td><td><button class="btn btn-primary" type="button" style="--bs-success: #198754;--bs-success-rgb: 25,135,84;">Notify</button></td></tr>'
            }
        });
}

function deleteItem(id) {
    fetch('https://digi-campus.herokuapp.com/api/security/student-delete/' + id, {
        method: 'DELETE',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        }
    }).then((response) => {
        buildList();
    })
}