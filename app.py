from flask import Flask, render_template
import analysis as anys

app = Flask(__name__)


def country_data_analysis(country):
    raw_chart_dict = anys.raw_chart(country)

    arima_data = anys.arima_model(country)
    
    data = [raw_chart_dict, arima_data]

    return data


@app.route("/")
def main_page():
    anys.get_worldmap()
    poll_dict = anys.find_max_for_worldmap()
    

    return render_template("index.html", pollution = poll_dict)

@app.route("/India")
def india():
    data = country_data_analysis("India")

    # For 1st chart
    raw_chart_dict = data[0]
    raw_chart_keys = list(raw_chart_dict.keys())
    raw_chart_vals = list(raw_chart_dict.values())

    # For ARIMA Chart
    arima_data = data[1]
    arima_orders = arima_data[2]
    arima_seasonal = arima_data[3]
    arima_errors = arima_data[1]
    arima_forecast = arima_data[0]

    arima_forecast_keys = list(arima_forecast.keys())
    arima_forecast_vals = list(arima_forecast.values())


    return render_template("India.html", 
    raw_chart_years = raw_chart_keys , raw_chart_vals = raw_chart_vals,
    arima_years = arima_forecast_keys, arima_vals = arima_forecast_vals, arima_errors = arima_errors, arima_orders = arima_orders, arima_seasonal = arima_seasonal, country = "India")

@app.route("/Canada")
def canada():
    data = country_data_analysis("Canada")

    # For 1st chart
    raw_chart_dict = data[0]
    raw_chart_keys = list(raw_chart_dict.keys())
    raw_chart_vals = list(raw_chart_dict.values())

    # For ARIMA Chart
    arima_data = data[1]
    arima_orders = arima_data[2]
    arima_seasonal = arima_data[3]
    arima_errors = arima_data[1]
    arima_forecast = arima_data[0]

    arima_forecast_keys = list(arima_forecast.keys())
    arima_forecast_vals = list(arima_forecast.values())


    return render_template("Canada.html", 
    raw_chart_years = raw_chart_keys , raw_chart_vals = raw_chart_vals,
    arima_years = arima_forecast_keys, arima_vals = arima_forecast_vals, arima_errors = arima_errors, arima_orders = arima_orders, arima_seasonal = arima_seasonal, country = "Canada")


@app.route("/China")
def china():
    data = country_data_analysis("China")

    # For 1st chart
    raw_chart_dict = data[0]
    raw_chart_keys = list(raw_chart_dict.keys())
    raw_chart_vals = list(raw_chart_dict.values())

    # For ARIMA Chart
    arima_data = data[1]
    arima_orders = arima_data[2]
    arima_seasonal = arima_data[3]
    arima_errors = arima_data[1]
    arima_forecast = arima_data[0]

    arima_forecast_keys = list(arima_forecast.keys())
    arima_forecast_vals = list(arima_forecast.values())


    return render_template("China.html", 
    raw_chart_years = raw_chart_keys , raw_chart_vals = raw_chart_vals,
    arima_years = arima_forecast_keys, arima_vals = arima_forecast_vals, arima_errors = arima_errors, arima_orders = arima_orders, arima_seasonal = arima_seasonal, country = "China")

@app.route("/Brazil")
def brazil():
    data = country_data_analysis("Brazil")

    # For 1st chart
    raw_chart_dict = data[0]
    raw_chart_keys = list(raw_chart_dict.keys())
    raw_chart_vals = list(raw_chart_dict.values())

    # For ARIMA Chart
    arima_data = data[1]
    arima_orders = arima_data[2]
    arima_seasonal = arima_data[3]
    arima_errors = arima_data[1]
    arima_forecast = arima_data[0]

    arima_forecast_keys = list(arima_forecast.keys())
    arima_forecast_vals = list(arima_forecast.values())


    return render_template("Brazil.html", 
    raw_chart_years = raw_chart_keys , raw_chart_vals = raw_chart_vals,
    arima_years = arima_forecast_keys, arima_vals = arima_forecast_vals, arima_errors = arima_errors, arima_orders = arima_orders, arima_seasonal = arima_seasonal, country = "Brazil")

@app.route("/United States")
def united_States():
    data = country_data_analysis("United States")

    # For 1st chart
    raw_chart_dict = data[0]
    raw_chart_keys = list(raw_chart_dict.keys())
    raw_chart_vals = list(raw_chart_dict.values())

    # For ARIMA Chart
    arima_data = data[1]
    arima_orders = arima_data[2]
    arima_seasonal = arima_data[3]
    arima_errors = arima_data[1]
    arima_forecast = arima_data[0]

    arima_forecast_keys = list(arima_forecast.keys())
    arima_forecast_vals = list(arima_forecast.values())


    return render_template("United_States.html", 
    raw_chart_years = raw_chart_keys , raw_chart_vals = raw_chart_vals,
    arima_years = arima_forecast_keys, arima_vals = arima_forecast_vals, arima_errors = arima_errors, arima_orders = arima_orders, arima_seasonal = arima_seasonal, country = "United States")

@app.route("/Afghanistan")
def afghanistan():
    data = country_data_analysis("Afghanistan")

    # For 1st chart
    raw_chart_dict = data[0]
    raw_chart_keys = list(raw_chart_dict.keys())
    raw_chart_vals = list(raw_chart_dict.values())

    # For ARIMA Chart
    arima_data = data[1]
    arima_orders = arima_data[2]
    arima_seasonal = arima_data[3]
    arima_errors = arima_data[1]
    arima_forecast = arima_data[0]

    arima_forecast_keys = list(arima_forecast.keys())
    arima_forecast_vals = list(arima_forecast.values())


    return render_template("Afghanistan.html", 
    raw_chart_years = raw_chart_keys , raw_chart_vals = raw_chart_vals,
    arima_years = arima_forecast_keys, arima_vals = arima_forecast_vals, arima_errors = arima_errors, arima_orders = arima_orders, arima_seasonal = arima_seasonal, country = "Afghanistan")

@app.route("/Australia")
def australia():

    data = country_data_analysis("Australia")

    # For 1st chart
    raw_chart_dict = data[0]
    raw_chart_keys = list(raw_chart_dict.keys())
    raw_chart_vals = list(raw_chart_dict.values())

    # For ARIMA Chart
    arima_data = data[1]
    arima_orders = arima_data[2]
    arima_seasonal = arima_data[3]
    arima_errors = arima_data[1]
    arima_forecast = arima_data[0]

    arima_forecast_keys = list(arima_forecast.keys())
    arima_forecast_vals = list(arima_forecast.values())


    return render_template("Australia.html", 
    raw_chart_years = raw_chart_keys , raw_chart_vals = raw_chart_vals,
    arima_years = arima_forecast_keys, arima_vals = arima_forecast_vals, arima_errors = arima_errors, arima_orders = arima_orders, arima_seasonal = arima_seasonal, country = "Australia")

@app.route("/Azerbaijan")
def azerbaijan():
    data = country_data_analysis("Azerbaijan")

    # For 1st chart
    raw_chart_dict = data[0]
    raw_chart_keys = list(raw_chart_dict.keys())
    raw_chart_vals = list(raw_chart_dict.values())

    # For ARIMA Chart
    arima_data = data[1]
    arima_orders = arima_data[2]
    arima_seasonal = arima_data[3]
    arima_errors = arima_data[1]
    arima_forecast = arima_data[0]

    arima_forecast_keys = list(arima_forecast.keys())
    arima_forecast_vals = list(arima_forecast.values())


    return render_template("Azerbaijan.html", 
    raw_chart_years = raw_chart_keys , raw_chart_vals = raw_chart_vals,
    arima_years = arima_forecast_keys, arima_vals = arima_forecast_vals, arima_errors = arima_errors, arima_orders = arima_orders, arima_seasonal = arima_seasonal, country = "Azerbaijan")

@app.route("/Egypt")
def egypt():
    data = country_data_analysis("Egypt")

    # For 1st chart
    raw_chart_dict = data[0]
    raw_chart_keys = list(raw_chart_dict.keys())
    raw_chart_vals = list(raw_chart_dict.values())

    # For ARIMA Chart
    arima_data = data[1]
    arima_orders = arima_data[2]
    arima_seasonal = arima_data[3]
    arima_errors = arima_data[1]
    arima_forecast = arima_data[0]

    arima_forecast_keys = list(arima_forecast.keys())
    arima_forecast_vals = list(arima_forecast.values())


    return render_template("Egypt.html", 
    raw_chart_years = raw_chart_keys , raw_chart_vals = raw_chart_vals,
    arima_years = arima_forecast_keys, arima_vals = arima_forecast_vals, arima_errors = arima_errors, arima_orders = arima_orders, arima_seasonal = arima_seasonal, country = "Egypt")

@app.route("/Germany")
def germany():
    data = country_data_analysis("Germany")

    # For 1st chart
    raw_chart_dict = data[0]
    raw_chart_keys = list(raw_chart_dict.keys())
    raw_chart_vals = list(raw_chart_dict.values())

    # For ARIMA Chart
    arima_data = data[1]
    arima_orders = arima_data[2]
    arima_seasonal = arima_data[3]
    arima_errors = arima_data[1]
    arima_forecast = arima_data[0]

    arima_forecast_keys = list(arima_forecast.keys())
    arima_forecast_vals = list(arima_forecast.values())


    return render_template("Germany.html", 
    raw_chart_years = raw_chart_keys , raw_chart_vals = raw_chart_vals,
    arima_years = arima_forecast_keys, arima_vals = arima_forecast_vals, arima_errors = arima_errors, arima_orders = arima_orders, arima_seasonal = arima_seasonal, country = "Germany")

@app.route("/Japan")
def japan():
    data = country_data_analysis("Japan")

    # For 1st chart
    raw_chart_dict = data[0]
    raw_chart_keys = list(raw_chart_dict.keys())
    raw_chart_vals = list(raw_chart_dict.values())

    # For ARIMA Chart
    arima_data = data[1]
    arima_orders = arima_data[2]
    arima_seasonal = arima_data[3]
    arima_errors = arima_data[1]
    arima_forecast = arima_data[0]

    arima_forecast_keys = list(arima_forecast.keys())
    arima_forecast_vals = list(arima_forecast.values())


    return render_template("Japan.html", 
    raw_chart_years = raw_chart_keys , raw_chart_vals = raw_chart_vals,
    arima_years = arima_forecast_keys, arima_vals = arima_forecast_vals, arima_errors = arima_errors, arima_orders = arima_orders, arima_seasonal = arima_seasonal, country = "Japan")

@app.route("/Libya")
def libya():
    data = country_data_analysis("Libya")

    # For 1st chart
    raw_chart_dict = data[0]
    raw_chart_keys = list(raw_chart_dict.keys())
    raw_chart_vals = list(raw_chart_dict.values())

    # For ARIMA Chart
    arima_data = data[1]
    arima_orders = arima_data[2]
    arima_seasonal = arima_data[3]
    arima_errors = arima_data[1]
    arima_forecast = arima_data[0]

    arima_forecast_keys = list(arima_forecast.keys())
    arima_forecast_vals = list(arima_forecast.values())


    return render_template("Libya.html", 
    raw_chart_years = raw_chart_keys , raw_chart_vals = raw_chart_vals,
    arima_years = arima_forecast_keys, arima_vals = arima_forecast_vals, arima_errors = arima_errors, arima_orders = arima_orders, arima_seasonal = arima_seasonal, country = "Libya")

@app.route("/Republic of the Congo")
def republic_of_the_Congo():
    data = country_data_analysis("Republic of the Congo")

    # For 1st chart
    raw_chart_dict = data[0]
    raw_chart_keys = list(raw_chart_dict.keys())
    raw_chart_vals = list(raw_chart_dict.values())

    # For ARIMA Chart
    arima_data = data[1]
    arima_orders = arima_data[2]
    arima_seasonal = arima_data[3]
    arima_errors = arima_data[1]
    arima_forecast = arima_data[0]

    arima_forecast_keys = list(arima_forecast.keys())
    arima_forecast_vals = list(arima_forecast.values())


    return render_template("Republic_of_the_Congo.html", 
    raw_chart_years = raw_chart_keys , raw_chart_vals = raw_chart_vals,
    arima_years = arima_forecast_keys, arima_vals = arima_forecast_vals, arima_errors = arima_errors, arima_orders = arima_orders, arima_seasonal = arima_seasonal, country = "Republic of the Congo")

@app.route("/Russia")
def russia():
    data = country_data_analysis("Russia")

    # For 1st chart
    raw_chart_dict = data[0]
    raw_chart_keys = list(raw_chart_dict.keys())
    raw_chart_vals = list(raw_chart_dict.values())

    # For ARIMA Chart
    arima_data = data[1]
    arima_orders = arima_data[2]
    arima_seasonal = arima_data[3]
    arima_errors = arima_data[1]
    arima_forecast = arima_data[0]

    arima_forecast_keys = list(arima_forecast.keys())
    arima_forecast_vals = list(arima_forecast.values())


    return render_template("Russia.html", 
    raw_chart_years = raw_chart_keys , raw_chart_vals = raw_chart_vals,
    arima_years = arima_forecast_keys, arima_vals = arima_forecast_vals, arima_errors = arima_errors, arima_orders = arima_orders, arima_seasonal = arima_seasonal, country = "Russia")

@app.route("/Saudi Arabia")
def saudi_Arabia():
    data = country_data_analysis("Saudi Arabia")

    # For 1st chart
    raw_chart_dict = data[0]
    raw_chart_keys = list(raw_chart_dict.keys())
    raw_chart_vals = list(raw_chart_dict.values())

    # For ARIMA Chart
    arima_data = data[1]
    arima_orders = arima_data[2]
    arima_seasonal = arima_data[3]
    arima_errors = arima_data[1]
    arima_forecast = arima_data[0]

    arima_forecast_keys = list(arima_forecast.keys())
    arima_forecast_vals = list(arima_forecast.values())


    return render_template("Saudi_Arabia.html", 
    raw_chart_years = raw_chart_keys , raw_chart_vals = raw_chart_vals,
    arima_years = arima_forecast_keys, arima_vals = arima_forecast_vals, arima_errors = arima_errors, arima_orders = arima_orders, arima_seasonal = arima_seasonal, country = "Saudi Arabia")

@app.route("/South Africa")
def south_Africa():
    data = country_data_analysis("South Africa")

    # For 1st chart
    raw_chart_dict = data[0]
    raw_chart_keys = list(raw_chart_dict.keys())
    raw_chart_vals = list(raw_chart_dict.values())

    # For ARIMA Chart
    arima_data = data[1]
    arima_orders = arima_data[2]
    arima_seasonal = arima_data[3]
    arima_errors = arima_data[1]
    arima_forecast = arima_data[0]

    arima_forecast_keys = list(arima_forecast.keys())
    arima_forecast_vals = list(arima_forecast.values())


    return render_template("South_Africa.html", 
    raw_chart_years = raw_chart_keys , raw_chart_vals = raw_chart_vals,
    arima_years = arima_forecast_keys, arima_vals = arima_forecast_vals, arima_errors = arima_errors, arima_orders = arima_orders, arima_seasonal = arima_seasonal, country = "South Africa")

@app.route("/South Korea")
def south_Korea():
    data = country_data_analysis("South Korea")

    # For 1st chart
    raw_chart_dict = data[0]
    raw_chart_keys = list(raw_chart_dict.keys())
    raw_chart_vals = list(raw_chart_dict.values())

    # For ARIMA Chart
    arima_data = data[1]
    arima_orders = arima_data[2]
    arima_seasonal = arima_data[3]
    arima_errors = arima_data[1]
    arima_forecast = arima_data[0]

    arima_forecast_keys = list(arima_forecast.keys())
    arima_forecast_vals = list(arima_forecast.values())


    return render_template("South_Korea.html", 
    raw_chart_years = raw_chart_keys , raw_chart_vals = raw_chart_vals,
    arima_years = arima_forecast_keys, arima_vals = arima_forecast_vals, arima_errors = arima_errors, arima_orders = arima_orders, arima_seasonal = arima_seasonal, country = "South Korea")

@app.route("/Turkey")
def turkey():
    data = country_data_analysis("Turkey")

    # For 1st chart
    raw_chart_dict = data[0]
    raw_chart_keys = list(raw_chart_dict.keys())
    raw_chart_vals = list(raw_chart_dict.values())

    # For ARIMA Chart
    arima_data = data[1]
    arima_orders = arima_data[2]
    arima_seasonal = arima_data[3]
    arima_errors = arima_data[1]
    arima_forecast = arima_data[0]

    arima_forecast_keys = list(arima_forecast.keys())
    arima_forecast_vals = list(arima_forecast.values())


    return render_template("Turkey.html", 
    raw_chart_years = raw_chart_keys , raw_chart_vals = raw_chart_vals,
    arima_years = arima_forecast_keys, arima_vals = arima_forecast_vals, arima_errors = arima_errors, arima_orders = arima_orders, arima_seasonal = arima_seasonal, country = "Turkey")

@app.route("/United Arab Emirates")
def united_Arab_Emirates():
    data = country_data_analysis("United Arab Emirates")

    # For 1st chart
    raw_chart_dict = data[0]
    raw_chart_keys = list(raw_chart_dict.keys())
    raw_chart_vals = list(raw_chart_dict.values())

    # For ARIMA Chart
    arima_data = data[1]
    arima_orders = arima_data[2]
    arima_seasonal = arima_data[3]
    arima_errors = arima_data[1]
    arima_forecast = arima_data[0]

    arima_forecast_keys = list(arima_forecast.keys())
    arima_forecast_vals = list(arima_forecast.values())


    return render_template("United_Arab_Emirates.html", 
    raw_chart_years = raw_chart_keys , raw_chart_vals = raw_chart_vals,
    arima_years = arima_forecast_keys, arima_vals = arima_forecast_vals, arima_errors = arima_errors, arima_orders = arima_orders, arima_seasonal = arima_seasonal, country = "United Arab Emirates")

@app.route("/United Kingdom")
def united_Kingdom():
    data = country_data_analysis("United Kingdom")

    # For 1st chart
    raw_chart_dict = data[0]
    raw_chart_keys = list(raw_chart_dict.keys())
    raw_chart_vals = list(raw_chart_dict.values())

    # For ARIMA Chart
    arima_data = data[1]
    arima_orders = arima_data[2]
    arima_seasonal = arima_data[3]
    arima_errors = arima_data[1]
    arima_forecast = arima_data[0]

    arima_forecast_keys = list(arima_forecast.keys())
    arima_forecast_vals = list(arima_forecast.values())


    return render_template("United_Kingdom.html", 
    raw_chart_years = raw_chart_keys , raw_chart_vals = raw_chart_vals,
    arima_years = arima_forecast_keys, arima_vals = arima_forecast_vals, arima_errors = arima_errors, arima_orders = arima_orders, arima_seasonal = arima_seasonal, country = "United Kingdom")

@app.route("/About")
def about():
    return render_template("About.html")

if __name__ == "__main__":
    app.run(debug=True)