from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/<name>')
def greet(name):
    return f"<h1>Hello, {name}!</h1>"

if __name__ == "__main__":
    app.run()