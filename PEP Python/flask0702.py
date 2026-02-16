from flask import Flask , request,jsonify
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    name = request.args.get("name","Flask")
    
    return f" Hello , {escape(name)}"

@app.route("/coustom")
def custom():
    name = request.args.get("para","cus")
    name = name.replace("<"," ")
    name = name.replace(">"," ")
    name = name.replace("/"," ")

    return f" Hello , {escape(name)}"

@app.route("/about")
def about():
    return "This is about page."
@app.route("/contact")
def contact():
    return "This is contact page."
@app.route("/login")
def login():
    return "This is login page."
@app.route("/signup")
def signup():
    return "This is sign up page."


app.run(debug=True)