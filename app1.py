import json
from flask import Flask, render_template, redirect, url_for, request
import os
import random


with open("database.txt", "r") as f:
    d = f.read()

    
database = json.loads(d)


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("database.html", database=database)


@app.route("/tag/<tag_name>")
def tag(tag_name):
    album = random.choice(database[tag_name])
    video_id = random.choice(album)
    return redirect("https://www.youtube.com/watch?v="+video_id)
    

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


