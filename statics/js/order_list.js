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
    var url = 'http://127.0.0.1:8000/api/security/student-list/';
    fetch(url)
        .then((resp) => resp.json())
        .then(function(data) {
            var list = data;
            for (var i in list) {
                if(list[i].in_hall == true) wrapper.innerHTML+='<tr><td>'+list[i].first_name+' '+list[i].last_name +'</td><td>'+list[i].room_visiting+'</td><td>'+(list[i].roll_no)+'</td><td>'+(list[i].mobile_no)+'</td><td><button class="btn btn-primary" type="button" style="--bs-success: #198754;--bs-success-rgb: 25,135,84;">Notify</button></td></tr>'
            }
        });
}
