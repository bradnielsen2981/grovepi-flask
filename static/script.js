/* This helper function sends and receive JSON to a server so to avoid a page refresh
urlstring, methodstring="GET"or"POST", parameterobject={var1:value,var1:value}, crossdomain=true or false, responsehandler=functionname */
function JQUERYajaxRequest(urlstring, methodstring, parametersobject=null, crossdomainbool=false, responsehandler=defaulthandler)
{
    $.ajax({
	    type: methodstring,
        crossDomain: crossdomainbool, //THIS IS REQUIRED IF COMMUNICATING TO NON-LOCAL SERVER
	    url: urlstring,
	    data: parametersobject, //{var1:1,var2:"hello"}
        dataType : "json",  //calls json.parse to convert results (JSON) to JavascriptObject
        success: responsehandler(results),
        error: function(error) {
           	console.log(error);
	    }
    });
}

//function responsehandler, receives the results object which has been converted from JSON
function defaulthandler(results)
{
    console.log(results);
}
