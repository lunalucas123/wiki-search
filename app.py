import requests
import json
from flask import Flask, redirect, url_for, render_template, request


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def word_input():
    if request.method == "POST":
        word = request.form["nm"]
        # print(word)
        return redirect(url_for("wiki_search",word=word))
    else:    
        return render_template("search_form.html")

@app.route("/<word>")    
def wiki_search(word):
    word = word.lower()
    word = word[0].upper() + word[1:]
    # print(word)
  
    data = requests.get(f"https://en.wikipedia.org/w/api.php?action=parse&format=json&page={word}")

    # print(type(data)) # <class 'requests.models.Response'>


    response_data = json.loads(data.text)


    
    title= response_data['parse']['title']
    my_list= response_data['parse']
   


    iwlinks = response_data['parse']['iwlinks']
    links_list = []
    for item in iwlinks:
        for key in item.keys():
            if key == 'url':
                links_list.append(item[key])

    # json_response = response_data['parse']
    # print(type(iwlinks))
    
    return render_template("Results.html",results={'title': title, 'mylist':my_list, 'iwlinks' : links_list }, link = f"https://en.wikipedia.org/w/api.php?action=parse&format=json&page={word}")        



if __name__ == "__main__":
    app.run(debug=True)


