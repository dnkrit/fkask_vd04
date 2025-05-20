from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    return render_template("index.html", current_time=now)

@app.route("/blog/")
def blog():
    return render_template("blog.html")

@app.route("/contacts/")
def contacts():
    return render_template("contacts.html")

if __name__ == "__main__":
    app.run(debug=True)
