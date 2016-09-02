<html>
<head>
<title>Decision Tree Results</title> 
 <link rel="stylesheet" type="text/css" href="design.css">
 <script type="text/javascript" src="https://www.google.com/jsapi"></script>
 <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
 <script src="jquery.csv-0.71.js"></script>
 <script>
	csvUrl= 'datasets.csv';
      // wait till the DOM is loaded
      $(function() {
         // grab the CSV
         $.get(csvUrl, function(csvString) {
            // display the contents of the CSV
            $("#chart").html(csvString);
         });
      });
   </script>
  
    <script type="text/javascript">
      
	  google.load('visualization', '1', {'packages': ['corechart']});
      google.setOnLoadCallback(initialize);
			
	   var queryOptions = {
		csvColumns: ['number', 'number' , 'number' /* Or whatever the columns in the CSV file are */],
		csvHasHeader: false /* This should be false if your CSV file doesn't have a header */
	  }
	  csvUrl= 'datasets.csv';
      function initialize() {
		$.get(csvUrl, function(csvString){
		var arrayData = $.csv.toArrays(csvString, {onParseValue: $.csv.hooks.castToScalar});
        var data = new google.visualization.arrayToDataTable(arrayData);
		var view = new google.visualization.DataView(data);
		view.setColumns([0,1]);
		var options = {
		title: "Average Flight Delays",
		hAxis: {title: data.getColumnLabel(0), minValue: data.getColumnRange(0).min, maxValue: data.getColumnRange(0).max},
		vAxis: {title: data.getColumnLabel(1), minValue: data.getColumnRange(1).min, maxValue: data.getColumnRange(1).max},
		legend: 'Average Delays'
		var chart = new google.visualization.ScatterChart(document.getElementById('chart'));
		chart.draw(view, options);
		}})
};
		
/*		// The URL of the spreadsheet to source data from.
      	var query = new google.visualization.Query(csvUrl,queryOptions);
        query.send(handleQueryResponse);
      }

      function handleQueryResponse(response){
	  
        if (response.isError()) {
          alert('Error in query');
        }
		
		var data = response.getDataTable();

		var query = new google.visualization.Query(csvUrl, opts);
		query.setQuery('select a, b where c = 1');
		
		var chart = new google.visualization.ColumnChart(
            document.getElementById('chart_div'));
        chart.draw(data, {'isStacked': true, 'legend': 'bottom',
            'vAxis': {'title': 'Average Delays'}});
		}*/
    </script>
</head> 

<body> 
<img src = "delay_calculator.jpg" alt = "delay_calculator" >

<?php 
echo "<h3> Results from the decision Tree </h3>"; 

$departure_airport .= $_POST["dep_airport"];
$arrival_airport .= $_POST["arr_airport"];
$departure_time = $_POST["from"];
$arrival_time = $_POST["to"];
settype($departure_airport, "string");
settype($arrival_airport, "string");
echo nl2br("Departure time from $departure_airport : $departure_time:00 hrs \n ");  
echo nl2br("Arrival time at $arrival_airport : $arrival_time:00 hrs \n "); 
//$result = shell_exec("python C:\Python27\bigdata.py C:\Python27\exportedOutput.csv 2 5");
//$command = escapeshellcmd("python C:\Python27\bigdata_new.py C:\Python27\final.csv $departure_time $arrival_time $departure_airport $arrival_airport"); 
$command = escapeshellcmd("python C:\Python27\bigdata.py C:\Python27\exportedOutput.csv $departure_time $arrival_time");
$output = shell_exec($command); 
echo nl2br("Result\n"); 
echo "<b>$output</b>\n"; 
?>
</body> </html>