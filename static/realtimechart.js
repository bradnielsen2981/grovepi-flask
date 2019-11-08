window.onload = function () { //make sure other scripts are loaded

    var dataPoints = [];
    
    var options = {
        theme: "light2",
        title: {
            text: "Live Chart from JSON Data"
        },
        data: [{
            type: "spline",
            dataPoints: dataPoints
        }]
    };
    
    $("#chartContainer").CanvasJSChart(options);
    updateData();
    
    // Initial Values
    var xValue = 0;
    var yValue = 10;
    var newDataCount = 6;
    
    function addData(data) {
        console.log(data)
        /*
        if (newDataCount != 1) {
            $.each(data, function (key, value) {
                dataPoints.push({ x: value[0], y: parseInt(value[1]) });
                xValue++;
                yValue = parseInt(value[1]);
            });
            newDataCount = 1;
        } else {
            //dataPoints.shift();
            dataPoints.push({ x: data[0][0], y: parseInt(data[0][1]) });
            xValue++;
            yValue = parseInt(data[0][1]);
        }
        $("#chartContainer").CanvasJSChart().render();
        */
        setTimeout(updateData, 1000);
    }
    
    function updateData() {
        JSONrequest('/realtimechart', "POST", addData)
    }
}