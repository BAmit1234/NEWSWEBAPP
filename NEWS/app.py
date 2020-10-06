from flask import Flask, render_template, jsonify

import json

app=Flask(__name__)
file=open("articles.json",'rb')
article=json.load(file)





@app.route("/")
def home():
        return render_template('home.html',data=article)
if __name__=="__main__":
    app.run()
