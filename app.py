from email import message
from flask import Flask , render_template, abort , jsonify #import flask 
from model import db
# from datetime import datetime
app = Flask(__name__)

@app.route("/") #rootv url and mapped to welcome medthod
def welcome():
    return render_template("welcome.html", cards=db )


@app.route("/card/<int:index>")
def card_view(index):
    try:

        card = db[index]
        return render_template("card.html", card=card,index=index, max_index = len(db)-1)
    except IndexError:
        abort(404) #if the index is not found


@app.route('/api/card/<int:index>')
def api_card_detail(index):
    try:
        return db[index]
    except IndexError:
        abort(404)

@app.route('/api/card')
def api_card_list():
    # return db direct return db doesnt work need to use jsonify to return whole list
    return jsonify(db)

# @app.route("/date")
# def date():
#     return "This page is served at " + str(datetime.now())

# counter=0
# @app.route("/count_views")
# def count_demo():
#     global counter
#     counter += 1
#     return "This page is served " + str(counter) + " times"