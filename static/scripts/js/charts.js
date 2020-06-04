function linen_graph() {
    google.charts.load('current', {'packages': ['corechart']});
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {
        var data = google.visualization.arrayToDataTable([
            ['Year', 'Бизнес', 'IT'],
            ['2013', 1000, 400],
            ['2014', 1170, 460],
            ['2015', 660, 1120],
            ['2016', 1030, 540]
        ]);

        var options = {
            legendTextStyle: {color: '#E4E4E4'},
            textStyle: {color: '#E4E4E4'},
            axisStyle: {color: '#E4E4E4'},
            titleTextStyle: {color: '#E4E4E4'},
            hAxis: {title: 'Year', textStyle: {color: '#E4E4E4'}, titleTextStyle: {color: '#E4E4E4'}},
            vAxis: {minValue: 0, textStyle: {color: '#E4E4E4'}, titleTextStyle: {color: '#E4E4E4'}},
            backgroundColor: '#2f2f2f',
        };

        var chart = new google.visualization.AreaChart(document.getElementById('chart_div'));
        chart.draw(data, options);
    }
}

function linen_category_graph() {
    google.charts.load('current', {'packages': ['corechart']});
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {
        var data = google.visualization.arrayToDataTable([
            ['Year', 'Бизнес', 'IT', 'Политика', 'Наука', 'Экономика'],
            ['2013', 1000, 400, 660, 1120, 540],
            ['2014', 1170, 460, 1000, 400, 480],
            ['2015', 660, 1120, 1000, 400, 1000],
            ['2016', 1030, 540, 660, 1120, 660]
        ]);

        var options = {
            legendTextStyle: {color: '#E4E4E4'},
            textStyle: {color: '#E4E4E4'},
            axisStyle: {color: '#E4E4E4'},
            titleTextStyle: {color: '#E4E4E4'},
            hAxis: {title: 'Year', textStyle: {color: '#E4E4E4'}, titleTextStyle: {color: '#E4E4E4'}},
            vAxis: {minValue: 0, textStyle: {color: '#E4E4E4'}, titleTextStyle: {color: '#E4E4E4'}},
            backgroundColor: '#2f2f2f',
        };

        var chart = new google.visualization.AreaChart(document.getElementById('linen_category_graph'));
        chart.draw(data, options);
    }
}

function category_pie_social() {
    google.charts.load('current', {'packages': ['corechart']});
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {

        var data = google.visualization.arrayToDataTable([
            ['Task', 'Hours per Day'],
            ['Бизнес', 11],
            ['IT', 2],
            ['Политика', 2],
            ['Наука', 2],
            ['Экономика', 7]
        ]);

        var options = {
            legendTextStyle: {color: '#E4E4E4'},
            textStyle: {color: '#E4E4E4'},
            axisStyle: {color: '#E4E4E4'},
            titleTextStyle: {color: '#E4E4E4'},
            hAxis: {title: 'Year', textStyle: {color: '#E4E4E4'}, titleTextStyle: {color: '#E4E4E4'}},
            vAxis: {minValue: 0, textStyle: {color: '#E4E4E4'}, titleTextStyle: {color: '#E4E4E4'}},
            backgroundColor: '#2f2f2f',
            chartArea:{width:"80%", height:"80%"}
        };

        var chart = new google.visualization.PieChart(document.getElementById('social_piechart'));

        chart.draw(data, options);
    }
}

function category_pie_browser() {
    google.charts.load('current', {'packages': ['corechart']});
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {

        var data = google.visualization.arrayToDataTable([
            ['Task', 'Hours per Day'],
            ['Бизнес', 11],
            ['IT', 2],
            ['Политика', 2],
            ['Наука', 2],
            ['Экономика', 7]
        ]);

        var options = {
            legendTextStyle: {color: '#E4E4E4'},
            textStyle: {color: '#E4E4E4'},
            axisStyle: {color: '#E4E4E4'},
            titleTextStyle: {color: '#E4E4E4'},
            hAxis: {title: 'Year', textStyle: {color: '#E4E4E4'}, titleTextStyle: {color: '#E4E4E4'}},
            vAxis: {minValue: 0, textStyle: {color: '#E4E4E4'}, titleTextStyle: {color: '#E4E4E4'}},
            backgroundColor: '#2f2f2f',
            chartArea:{width:"80%", height:"80%"}
        };

        var chart = new google.visualization.PieChart(document.getElementById('browser_piechart'));

        chart.draw(data, options);
    }
}