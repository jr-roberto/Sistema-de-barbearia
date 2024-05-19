from flask import Flask, jsonify, render_template

app = Flask(__name__)

users = [{"username":"Roberto","password":"123mudar!"}]

@app.route("/")
@app.route("/login")
def index():
    return render_template("index.html")

@app.route("/logon", methods=["POST"])
def logon():
    return jsonify(200)
