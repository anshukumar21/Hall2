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
    var wrapper = document.getElementById('idhar');
    wrapper.innerHTML = "";
    var url = 'https://digi-campus.herokuapp.com/api/main_extras_list/';
    fetch(url)
        .then((resp) => resp.json())
        .then(function(data) {
            var list = data;
            for (var i in list) {
                var item = '<div class="card" id="data-row-' + i + '" style="border-radius: 20px;background: #f2f5fe;border-bottom-width: 12px;border-bottom-color: rgb(178,185,236);box-shadow: 0px 35px 51px #b2b9ec;margin-bottom: 16px;margin-top: 16px;"><div class="card-body"><div class="row"><div class="col d-flex" style="width: 25%;"><p class="d-md-flex d-xxl-flex justify-content-md-center align-items-md-center align-items-xxl-center" style="width: 100%;text-align: left;font-family: Nunito, sans-serif;margin-bottom: 0px;margin-top: 0px;color: rgb(0,0,0);">' + list[i].extras_1 + '</p></div><div class="col d-flex" style="width: 25%;"><p class="d-md-flex d-xxl-flex justify-content-md-center align-items-md-center align-items-xxl-center" style="width: 100%;text-align: left;font-family: Nunito, sans-serif;margin-bottom: 0px;margin-top: 0px;color: rgb(0,0,0);">Extra</p></div><div class="col d-md-flex d-xxl-flex justify-content-md-center align-items-md-center justify-content-xxl-center align-items-xxl-center" style="width: 25%;"><p class="d-xxl-flex align-items-xxl-center" style="width: 100%;text-align: left;font-family: Nunito, sans-serif;margin-bottom: 0px;margin-top: 0px;color: rgb(0,0,0);"><i class="fa fa-inr" aria-hidden="true"></i>' + list[i].price_1 + '</p></div><div class="col d-md-flex d-xxl-flex justify-content-md-center align-items-md-center justify-content-xxl-end align-items-xxl-center" style="width: 25%;"><button class="btn btn-danger" onclick="deleteItem(' + list[i].id + ')" type="button" style="border-radius: 8px;border-width: 0px;background: #f13b3b;"><i class="fa fa-close"></i></button></div></div></div></div>';
                wrapper.innerHTML += item;
            }
        });
    url = 'https://digi-campus.herokuapp.com/api/main_menu_list/';
    fetch(url)
        .then((resp) => resp.json())
        .then(function(data) {
            var list = data;
            for (var i in list) {
                var item = '<div class="card" id="mess-row-' + i + '" style="border-radius: 20px;background: #f2f5fe;border-bottom-width: 12px;border-bottom-color: rgb(178,185,236);box-shadow: 0px 35px 51px #b2b9ec;margin-bottom: 16px;margin-top: 16px;"><div class="card-body"><div class="row"><div class="col d-flex" style="width: 25%;"><p class="d-md-flex d-xxl-flex justify-content-md-center align-items-md-center align-items-xxl-center" style="width: 100%;text-align: left;font-family: Nunito, sans-serif;margin-bottom: 0px;margin-top: 0px;color: rgb(0,0,0);">' + list[i].main_1 + '</p></div><div class="col d-flex" style="width: 25%;"><p class="d-md-flex d-xxl-flex justify-content-md-center align-items-md-center align-items-xxl-center" style="width: 100%;text-align: left;font-family: Nunito, sans-serif;margin-bottom: 0px;margin-top: 0px;color: rgb(0,0,0);">Basic</p></div><div class="col d-md-flex d-xxl-flex justify-content-md-center align-items-md-center justify-content-xxl-center align-items-xxl-center" style="width: 25%;"><p class="d-xxl-flex align-items-xxl-center" style="width: 100%;text-align: left;font-family: Nunito, sans-serif;margin-bottom: 0px;margin-top: 0px;color: rgb(0,0,0);"><i class="fa fa-inr" aria-hidden="true"></i>' + list[i].price_1 + '</p></div><div class="col d-md-flex d-xxl-flex justify-content-md-center align-items-md-center justify-content-xxl-end align-items-xxl-center" style="width: 25%;"><button class="btn btn-danger" type="button" style="border-radius: 8px;border-width: 0px;background: #f13b3b;"><i class="fa fa-close"></i></button></div></div></div></div>';
                wrapper.innerHTML += item;
            }
        })
}

function update_list() {
    var if_extras = document.getElementById('check');
    if (if_extras.checked) update_extra_list();
    //if (if_extras =="on") update_extra_list();
    else update_main_list();
}

function update_main_list() {
    var url = 'https://digi-campus.herokuapp.com/api/main_menu_create/';
    var name = document.getElementById('name').value;
    var price = document.getElementById('price').value;
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'id': 1,
            'main_1': name,
            'price_1': price,
            'hall_number': 5,
        })
    }).then(function(response) {
        buildList();
    })
}

function update_extra_list() {
    var url = 'https://digi-campus.herokuapp.com/api/main_extras_create/';
    var name = document.getElementById('name').value;
    var price = document.getElementById('price').value;
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            "id": 1,
            "extras_1": name,
            "price_1": price,
            "hall_number": 5
        })
    }).then(function(response) {
        buildList();
    })
}

function deleteItem(id) {
    fetch('https://digi-campus.herokuapp.com/api/main_extras_delete/' + id, {
        method: 'DELETE',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        }
    }).then((response) => {
        buildList();
    })
}