from flask import Flask, render_template, send_from_directory
import os

app = Flask(
    __name__, template_folder="gamerevs/templates", static_folder="gamerevs/static"
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/games")
def games():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("index.html")


@app.route("/game/<int:game_id>")
def game_detail(game_id):
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
