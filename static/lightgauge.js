//GAUGE CODE-----------------------------------------------------------
//Google Charts - Gauge

var recurringhandle2 = null;
google.charts.load('current', {'packages':['gauge']});
google.charts.setOnLoadCallback(function(){ recurringhandle2 = setInterval(get_gauge_data, 5000); } );

function draw_gauge(result) {

    var options = {
        width: 400, height: 120,
        redFrom: 800, redTo: 1000,
        yellowFrom:500, yellowTo: 800,
        minorTicks: 5, max:1000
    };

    var data = google.visualization.arrayToDataTable([
        ['Label', 'Value'],
        ['Light', 300]
    ]);
    data.setValue(0, 1, result.Light);

    var chart = new google.visualization.Gauge(document.getElementById('light_gauge_chart'));
    chart.draw(data, options);

}

//THis recurring function gets data using JSON
function get_gauge_data() {
    JSONrequest('/getlight','POST', draw_gauge); //Once data is received, send to draw
}

//----------------------------------------------------------