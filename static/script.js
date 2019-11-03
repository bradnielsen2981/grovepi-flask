function ajaxRequest(url) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url);

    xhr.onload = function() {
        if (xhr.status === 200) {
            console.log('Response Text: ' + xhr.responseText);
            document.getElementById("message").innerHTML = "the " + url.slice(1) + " thread is active";
        } else {
            console.log('Request failed.  Returned status of: ' + xhr.status);
        }
    };
    xhr.send();
}