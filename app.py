import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient

def create_app():
    app = Flask(__name__)
    client = MongoClient("mongodb+srv://tawadev:tawadev@2021@cluster0.6geuj.mongodb.net/fullstack?retryWrites=true&w=majority")
    app.db = client.microblog


    @app.route("/",methods=["GET","POST"])
    def home():
        if request.method == "POST":
            entry_content = request.form.get("content")
            fdate = datetime.datetime.today().strftime("%Y-%m-%d")
            app.db.article.insert({"content":entry_content,"date":fdate})

        entries_with_dates = [(entry["content"],entry["date"],datetime.datetime.strptime(entry["date"],"%Y-%m-%d").strftime("%b %d")) for entry in app.db.article.find({})]    
        return render_template("index.html",entries=entries_with_dates) 

    return app
