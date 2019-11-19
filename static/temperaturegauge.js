//GAUGE CODE-----------------------------------------------------------
//Google Charts - Gauge

var recurringhandle2 = null;
google.charts.load('current', {'packages':['gauge']});
google.charts.setOnLoadCallback(function(){ recurringhandle2 = setInterval(get_temp_gauge_data, 5000); } );

function draw_temp_gauge(result) {

    var options = {
        width: 400, height: 120,
        redFrom: 70, redTo: 100,
        yellowFrom:40, yellowTo: 70,
        minorTicks: 5, max:100
    };

    var data = google.visualization.arrayToDataTable([
        ['Label', 'Value'],
        ['Temperature', 30]
    ]);
    data.setValue(0, 1, result.Temperature);

    var chart = new google.visualization.Gauge(document.getElementById('temp_gauge_chart'));
    chart.draw(data, options);

}

//THis recurring function gets data using JSON
function get_temp_gauge_data() {
    JSONrequest('/gettemphumidity','POST', draw_temp_gauge); //Once data is received, send to draw
}

//----------------------------------------------------------