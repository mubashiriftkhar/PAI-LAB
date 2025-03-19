from flask import Flask, render_template
import requests

app = Flask(__name__)

jokeEndPoint = "https://official-joke-api.appspot.com/random_joke"

@app.route("/")
def index():
   
    response = requests.get(jokeEndPoint)
    if response.status_code == 200:
        joke = response.json()
    else:
        joke = {"setup": "Failed to fetch joke", "punchline": "Please try again later."}
    return render_template("index.html", joke=joke)

if __name__ == "__main__":
    app.run(debug=True)