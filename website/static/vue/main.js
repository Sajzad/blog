function sendRequest(url, method, data){
    var r = axios({
        method:method,
        url: url,
        data: data,
        xsrfCookieName:'csrftoken',
        xsrfHeaderName:'X-CSRFToken',
        headers:{
            'X-Requested-With':'XMLHttpRequest'
        }
    })
    return r
}
