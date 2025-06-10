
var ctx = document.getElementById("myChart");
var chart = new Chart(ctx, {
  type: "bar",
  data: {
    labels: ["2020/02/17", "", "2020/02/23", "", "2020/02/29", ""],
    datasets: [
      {
        type: "bar",
        backgroundColor: "rgba(54, 162, 235, 0.2)",
        borderColor: "rgba(54, 162, 235, 1)",
        borderWidth: 1,
        label: "A",
        data: [60, 49, 72, 90, 100, 60]
      },
	  {
        type: "bar",
        backgroundColor:  "rgba(100, 7.84, 57.65, 0.2)",
        borderColor: "rgba(100, 7.84, 57.65, 1)",
        borderWidth: 1,
        label: "B",
        data: [80, 20, 15, 45, 60, 30]
      },
      {
        type: "line",
        label: "C",
        data: [25, 13, 30, 35, 25, 40],
        lineTension: 0, 
        fill: false ,
		borderColor:"red"
      },
	  {
        type: "line",
        label: "D",
        data: [30, 45, 20, 5, 25, 15],
        lineTension: 0, 
        fill: false,
		borderColor:"green"
      }
    ]
  }
});
