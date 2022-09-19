from email import message
from urllib import request
from flask import Flask , render_template, abort , jsonify, request , redirect, url_for#import flask 
from model import db, save_db
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
    # return db "direct return db doesnt work need to use jsonify to return whole list"
    return jsonify(db)

@app.route('/addcard', methods=["GET","POST"])
def add_card():
    if request.method == "POST":
        card = {"question" : request.form['Question'], "answer" : request.form['Answer']}
        db.append(card)
        save_db()
        return redirect(url_for('card_view', index = len(db)-1))
    else:
        return render_template('add_card.html')

@app.route('/deletecard/<int:index>', methods=["GET","POST"])
def delete_card(index):
    try:
        if request.method == "POST":
            del db[index]
            save_db()
            return redirect(url_for('welcome'))
    
        else:
            return render_template('delete_card.html', card = db[index])
    except IndexError:
        abort(404)
# @app.route("/date")
# def date():
#     return "This page is served at " + str(datetime.now())

# counter=0
# @app.route("/count_views")
# def count_demo():
#     global counter
#     counter += 1
#     return "This page is served " + str(counter) + " times"