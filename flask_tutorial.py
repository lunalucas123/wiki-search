import requests
import json
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template("index.html")

@app.route("/", methods=["POST", "GET"])
def artist_input():
    if request.method == "POST":
        artist = request.form["nm"]
        return redirect(url_for("artist_search", artist=artist))
    else:    
        return render_template("search_form.html")

@app.route("/<artist>")    
def artist_search(artist):
    artist = artist.replace(' ', '+').upper()

    response = requests.get(f"https://itunes.apple.com/search?term={artist}&limit=5")
    obj = response.json()
    # return obj
    list_of_dicts = obj['results']
    return render_template("response.html", content = list_of_dicts)
    # list_of_dicts = obj['results']
    # for i in list_of_dicts:
    #     return 'Artist = ' +  i['artistName'] + '\n' + 'track name = ' + i['trackName'] + '\n' +'Hear Preview = ' + i['previewUrl'] 
    # return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run(debug=True)


