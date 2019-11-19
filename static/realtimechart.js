// Visualization API with the 'corechart' package.
var recurringhandle = null;  //can be used to delete recurring function
google.charts.load('visualization', { packages: ['corechart'] });
google.charts.setOnLoadCallback(function(){ recurringhandle = setInterval(get_line_chart_data, 1000); }); //starts the line chart
var SensorList = [];

//with received json data, draw the chart
function draw_line_chart(result) {
    //Formatting options for the graph
    var line_chart_options = { title: 'Light', curveType: 'function', legend: { position: 'bottom', textStyle: { color: '#555', fontSize: 14} } };
    //Sensor data will be pushed into this array
    var line_chart_headings = ['Time', 'Light', 'Temperature'];

    // LIVE DATA - add the data to the sensor array
    if (SensorList.length == 0) { SensorList.push(line_chart_headings); }
    listlength = SensorList.push([result.Time, result.Light, result.Temperature]);
    if (listlength > 20) { 
        SensorList.shift(); SensorList.shift(); //delete first two elements of array
        SensorList.unshift(line_chart_headings); //Add the headings back
    } 
    // Create DataTable and add the array to it.
    console.log(SensorList);
    var figures = google.visualization.arrayToDataTable(SensorList);

    // Define the chart type (LineChart) and the container (a DIV in our case).
    var chart = new google.visualization.LineChart(document.getElementById('line_chart'));
    chart.draw(figures, line_chart_options);     
}

//THis recurring function gets data using JSON
function get_line_chart_data() {
    JSONrequest('/realtimechart','POST', draw_line_chart); //Once data is received it is passed to the drawchart function
}



//GAUGE CODE-----------------------------------------------------------
//Google Charts - Gauge
/*
var recurringhandle2 = null;
google.charts.load('current', {'packages':['gauge']});
google.charts.setOnLoadCallback(function(){ recurringhandle2 = setInterval(get_gauge_data, 1000); } );

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

    var chart = new google.visualization.Gauge(document.getElementById('gauge_chart'));
    chart.draw(data, options);

}

//THis recurring function gets data using JSON
function get_gauge_data() {
    JSONrequest('/getlight','POST', draw_gauge); //Once data is received, send to draw
}
*/
//----------------------------------------------------------