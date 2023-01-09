from flask import Flask, render_template
import requests, json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def greet():
    weather = requests.get("https://weathertng.vercel.app/api")
    data = weather.json()
    degree = float(data['WEATHER']) - 273.15 
    degreestr = str(degree)
    return render_template("about.html", WEATHER=degreestr[:4])

@app.route('/contact')
def contact():
    return render_template("contact.html")
    
if __name__ == "__main__":
    app.run()