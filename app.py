import random
from flask import Flask, jsonify, render_template

app = Flask(__name__)

RESPONSES = [
    ("It is certain.", "positive"),
    ("It is decidedly so.", "positive"),
    ("Without a doubt.", "positive"),
    ("Yes, definitely.", "positive"),
    ("You may rely on it.", "positive"),
    ("As I see it, yes.", "positive"),
    ("Most likely.", "positive"),
    ("Outlook good.", "positive"),
    ("Yes.", "positive"),
    ("Signs point to yes.", "positive"),
    ("Reply hazy, try again.", "neutral"),
    ("Ask again later.", "neutral"),
    ("Better not tell you now.", "neutral"),
    ("Cannot predict now.", "neutral"),
    ("Concentrate and ask again.", "neutral"),
    ("Don't count on it.", "negative"),
    ("My reply is no.", "negative"),
    ("My sources say no.", "negative"),
    ("Outlook not so good.", "negative"),
    ("Very doubtful.", "negative"),
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/shake")
def shake():
    answer, response_type = random.choice(RESPONSES)
    return jsonify({"answer": answer, "type": response_type})


if __name__ == "__main__":
    app.run(debug=True)
