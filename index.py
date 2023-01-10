from flask import Flask, render_template
import requests, json

app = Flask(__name__)

def get_time():
    r = requests.get("https://timeapi.io/api/Time/current/zone?timeZone=Asia/Jakarta")
    time_data = r.json()
    return time_data['time']

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def greet():
    weather = requests.get("https://weathertng.vercel.app/api")
    data = weather.json()
    degree = float(data['WEATHER']) - 273.15 
    degreestr = str(degree)
    time = get_time()
    return render_template("about.html", WEATHER=degreestr[:4], TIME=time)

@app.route('/contact')
def contact():
    return render_template("contact.html")
    
if __name__ == "__main__":
    app.run()