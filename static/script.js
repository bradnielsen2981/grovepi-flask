//need to import jquery scripts

//simple ajax get request
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

//url, method="GET"or"POST", parameterobject=javascript object, crossdomain=true or false, 
function JQUERYajaxRequest(urlstring, methodstring, parametersobject, crossdomainbool, responsehandler)
{
    $.ajax({
	    type: method,
        crossDomain: crossdomainbool, //THIS IS REQUIRED IF COMMUNICATING TO NON LOCAL SERVER
	    url: url,
	    data: parametersobject, //{ var1:1,var2:"hello"  }
        dataType : "json",  //calls json.parse to convert results (JSON) to JavascriptObject
        success: responsehandler(results),
        error: function(error) {
           	console.log(error);
	    }
    });
}
