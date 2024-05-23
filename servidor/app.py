from flask import Flask, jsonify, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key = "dev"

users = [{"username":"Roberto","password":"!SenhaSecreta123@"}]

def realizando_login(username:str, password:str):
    for i in users:
        if i["username"] == username and i["password"] == password:
            return {"valid":True,"message":"Login realizado com sucesso.","username":username}

    return {"valid":False,"message":"Dados de login nao conferem"}

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

@app.route("/", endpoint="home")
@app.route("/login", endpoint="login")
def index():
    return render_template("index.html")

@app.route("/painel")
def painel():
    try:
        result_login=session['result_login']
        return render_template("painel.html",result_login=result_login)

    except:
        return redirect(url_for('login'))

@app.route("/logon", methods=["POST","GET"])
def logon():
    if request.method == 'GET':
        return redirect(url_for('login'))

    form = request.form
    result_login=realizando_login(form["username"],form["password"])

    if result_login['valid']:
        session['result_login']=result_login
        return redirect(url_for('painel'))

    return render_template("index.html",erro_login=result_login)

@app.route("/logoff")
def logoff():
    session.pop('result_login')
    return redirect(url_for('login'))
