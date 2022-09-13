from email import message
from flask import Flask , render_template, abort  #import flask 
from model import db
# from datetime import datetime
app = Flask(__name__)

@app.route("/") #rootv url and mapped to welcome medthod
def welcome():
    return render_template("welcome.html", message = "This is roopa just checking jinja variables and this message comes from view. ")


@app.route("/card/<int:index>")
def card_view(index):
    try:

        card = db[index]
        return render_template("card.html", card=card)
    except IndexError:
        abort(404) #if the index is not found






# @app.route("/date")
# def date():
#     return "This page is served at " + str(datetime.now())

# counter=0
# @app.route("/count_views")
# def count_demo():
#     global counter
#     counter += 1
#     return "This page is served " + str(counter) + " times"