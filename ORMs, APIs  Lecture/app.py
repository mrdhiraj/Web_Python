from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    return "Hello"


@app.route("/calendar")
def calendar():
    return "Comming Soon!"


@app.route("/calendar/<string:year>")
def calendars(year):
    return "<b>Comming Soon!<b>" + year



@app.route("/trytemplate")
def trytemplate():
    return render_template("template.html")


@app.route("/trytemplates/<string:year>")
def trytemplateagain(year):
    return render_template("template.html",templateyear =year)
