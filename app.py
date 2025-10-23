from flask import *
import os,json
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.expanduser("C:/Users/Hp/Documents/GitHub/updesh_secrets/.env"))

firebase_key = os.getenv('FIREBASE_CREDENTIALS')

print("\nkey : ",firebase_key)

app = Flask(__name__)

@app.route("/")

def home():
    return render_template("index.html")



@app.route("/login")

def login():
    return render_template("login.html")






app.run(debug=True)
