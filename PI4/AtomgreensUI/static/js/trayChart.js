
    var phData = {
        labels :  ['9:00 AM', '9:10 AM', '9:20 AM', '9:30 AM', '9:40 AM', '9:50 AM', '10:00 AM'],

        datasets: [{
            label: 'PH of Water',
            borderColor: ['rgb(73,143,133)', 'rgb(41,98,98)'],
            data : [14, 7, 12, 2, 5, 10, 8],
            fill: false,
        }]
    }

    var ctx1 = document.getElementById('phChart').getContext('2d');
    ctx1.canvas.width = 1000;
    ctx1.canvas.height = 250;
    var phChart = new Chart(ctx1, {
			type: 'line',
			data: phData,
		});

    window.randomScalingFactor = function() {
      return Math.random();
    };

    var ctx2 = document.getElementById('ecChart').getContext('2d');
    ctx2.canvas.width = 1000;
    ctx2.canvas.height = 250;
    var ecChart = new Chart(ctx2, {
			type: 'line',
			data: {
                labels: ['9:00 AM', '9:10 AM', '9:20 AM', '9:30 AM', '9:40 AM', '9:50 AM', '10:00 AM'],
                datasets: [{
                    label: 'EC of Water',
                    borderColor: [
                        'rgb(195,178,98)',
                        'rgb(98,89,41)'
                    ],
                    data: [(randomScalingFactor()),
                        (randomScalingFactor()),
                        (randomScalingFactor()),
                        (randomScalingFactor()),
                        (randomScalingFactor()),
                        (randomScalingFactor()),
                        (randomScalingFactor())],
                    fill: false,
                }],
                options: {
                    responsive: false,
                    maintainAspectRatio: false,
                    scales: {
                        yAxes: [{
                            ticks: {
                                // the data minimum used for determining the ticks is Math.min(dataMin, suggestedMin)
                                suggestedMin: 0,

                                // the data maximum used for determining the ticks is Math.max(dataMax, suggestedMax)
                                suggestedMax: 15
                            }
                        }]
                    }
                }
            }
		});

    var ctx3 = document.getElementById('weightChart').getContext('2d');
    ctx3.canvas.width = 1000;
    ctx3.canvas.height = 250;
    var weightChart = new Chart(ctx3, {
			type: 'line',
			data: {
                labels: ['9:00 AM', '9:10 AM', '9:20 AM', '9:30 AM', '9:40 AM', '9:50 AM', '10:00 AM'],
                datasets: [{
                    label: 'Weight',
                    borderColor: [
                        'rgb(87,143,73)',
                        'rgb(47,98,41)'
                    ],
                    data: [randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor()],
                    fill: false,
                }],
                options: {
                    responsive: false,
                    maintainAspectRatio: false,
                    scales: {
                        yAxes: [{
                            ticks: {
                                // the data minimum used for determining the ticks is Math.min(dataMin, suggestedMin)
                                suggestedMin: 70,

                                // the data maximum used for determining the ticks is Math.max(dataMax, suggestedMax)
                                suggestedMax: 90
                            }
                        }]
                    }
                }
            }
		});

    var ctx4 = document.getElementById('intempChart').getContext('2d');
    ctx4.canvas.width = 1000;
    ctx4.canvas.height = 250;
    var intempChart = new Chart(ctx4, {
			type: 'line',
			data: {
                labels: ['9:00 AM', '9:10 AM', '9:20 AM', '9:30 AM', '9:40 AM', '9:50 AM', '10:00 AM'],
                datasets: [{
                    label: 'Internal Temperature (°F)',
                    borderColor: [
                        'rgb(86,73,143)',
                        'rgb(56,41,98)'
                    ],
                    data: [Math.floor(Math.random() * 10) + 77,
                        Math.floor(Math.random() * 10) + 77,
                        Math.floor(Math.random() * 10) + 77,
                        Math.floor(Math.random() * 10) + 77,
                        Math.floor(Math.random() * 10) + 77,
                        Math.floor(Math.random() * 10) + 77,
                        Math.floor(Math.random() * 10) + 77],
                    fill: false,
                }],
                options: {
                    responsive: false,
                    maintainAspectRatio: false,
                    scales: {
                        yAxes: [{
                            ticks: {
                                // the data minimum used for determining the ticks is Math.min(dataMin, suggestedMin)
                                suggestedMin: 70,

                                // the data maximum used for determining the ticks is Math.max(dataMax, suggestedMax)
                                suggestedMax: 90
                            }
                        }]
                    }
                }
            }
		});

     var ctx5 = document.getElementById('humtempChart').getContext('2d');
     ctx5.canvas.width = 1000;
     ctx5.canvas.height = 250;
    var humtempChart = new Chart(ctx5, {
			type: 'line',
			data: {
                labels: ['9:00 AM', '9:10 AM', '9:20 AM', '9:30 AM', '9:40 AM', '9:50 AM', '10:00 AM'],
                datasets: [{
                    label: 'Humidity',
                    borderColor: [
                        'rgb(184,131,74)',
                        'rgb(98,68,41)'
                    ],
                    data: [Math.floor(Math.random() * 10) + 40,
                        Math.floor(Math.random() * 10) + 40,
                        Math.floor(Math.random() * 10) + 40,
                        Math.floor(Math.random() * 10) + 40,
                        Math.floor(Math.random() * 10) + 40,
                        Math.floor(Math.random() * 10) + 40,
                        Math.floor(Math.random() * 10) + 40],
                    fill: false,
                }],
                options: {
                    responsive: false,
                    maintainAspectRatio: false,
                    scales: {
                        yAxes: [{
                            ticks: {
                                // the data minimum used for determining the ticks is Math.min(dataMin, suggestedMin)
                                suggestedMin: 40,

                                // the data maximum used for determining the ticks is Math.max(dataMax, suggestedMax)
                                suggestedMax: 60
                            }
                        }]
                    }
                }
            }
		});

    var ctx6 = document.getElementById('extempChart').getContext('2d');
    ctx6.canvas.width = 1000;
    ctx6.canvas.height = 250;
    var extempChart = new Chart(ctx6, {
			type: 'line',
			data: {
                labels: ['9:00 AM', '9:10 AM', '9:20 AM', '9:30 AM', '9:40 AM', '9:50 AM', '10:00 AM'],
                datasets: [{
                    label: 'External Temperature (°F)',
                    borderColor: [
                        'rgb(40,72,32)',
                        'rgb(66,157,54)'
                    ],
                    data: [Math.floor(Math.random() * 10) + 77,
                        Math.floor(Math.random() * 10) + 77,
                        Math.floor(Math.random() * 10) + 77,
                        Math.floor(Math.random() * 10) + 77,
                        Math.floor(Math.random() * 10) + 77,
                        Math.floor(Math.random() * 10) + 77,
                        Math.floor(Math.random() * 10) + 77],
                    fill: false,
                }],
                options: {
                    responsive: false,
                    maintainAspectRatio: false,
                    scales: {
                        yAxes: [{
                            ticks: {
                                // the data minimum used for determining the ticks is Math.min(dataMin, suggestedMin)
                                suggestedMin: 70,

                                // the data maximum used for determining the ticks is Math.max(dataMax, suggestedMax)
                                suggestedMax: 90
                            }
                        }]
                    }
                }
            }
		});

    var ctx7 = document.getElementById('redChart').getContext('2d');
    ctx7.canvas.width = 1000;
    ctx7.canvas.height = 250;
    var redChart = new Chart(ctx7, {
			type: 'line',
			data: {
                labels: ['9:00 AM', '9:10 AM', '9:20 AM', '9:30 AM', '9:40 AM', '9:50 AM', '10:00 AM'],
                datasets: [{
                    label: 'Lighting Power (Red)',
                    borderColor: [
                        'rgb(143,73,75)',
                        'rgb(98,41,48)'
                    ],
                    data: [randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor()],
                    fill: false,
                }],
                options: {
                    responsive: false,
                    maintainAspectRatio: false,
                    scales: {
                        yAxes: [{
                            ticks: {
                                // the data minimum used for determining the ticks is Math.min(dataMin, suggestedMin)
                                suggestedMin: 70,

                                // the data maximum used for determining the ticks is Math.max(dataMax, suggestedMax)
                                suggestedMax: 90
                            }
                        }]
                    }
                }
            }
		});

    var ctx8 = document.getElementById('blueChart').getContext('2d');
    ctx8.canvas.width = 1000;
    ctx8.canvas.height = 250;
    var blueChart = new Chart(ctx8, {
			type: 'line',
			data: {
                labels: ['9:00 AM', '9:10 AM', '9:20 AM', '9:30 AM', '9:40 AM', '9:50 AM', '10:00 AM'],
                datasets: [{
                    label: 'Lighting Power (Blue)',
                    borderColor: [
                        'rgb(73,123,143)',
                        'rgb(41,62,98)'
                    ],
                    data: [randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor()],
                    fill: false,
                }],
                options: {
                    responsive: false,
                    maintainAspectRatio: false,
                    scales: {
                        yAxes: [{
                            ticks: {
                                // the data minimum used for determining the ticks is Math.min(dataMin, suggestedMin)
                                suggestedMin: 70,

                                // the data maximum used for determining the ticks is Math.max(dataMax, suggestedMax)
                                suggestedMax: 90
                            }
                        }]
                    }
                }
            }
		});


