const valid_data = function(){
    let username = $('#username').val()
    let password = $('#password').val()
    if(username == '' || password == ''){
        alert('入力されていない項目があります')
        return false
    }
}