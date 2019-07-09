from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)

#################################################
# Flask Routes
#################################################  
    
# Renders index page
@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/cloudiness")
def cloudiness():
    return render_template("cloudiness.html")
    
@app.route("/temperature")
def temperature():
    return render_template("temperature.html")

@app.route("/humidity")
def humidity():
    return render_template("humidity.html")

@app.route("/windspeed")
def windspeed():
    return render_template("humidity.html")

@app.route("/comparison")
def comparison():
    return render_template("comparison.html")

@app.route("/data")
def data():
    return render_template("data.html")

if __name__ == "__main__":
    app.run(host= '0.0.0.0')
    
