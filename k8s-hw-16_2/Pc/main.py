from flask import Flask
import requests



app = Flask(__name__)

@app.get('/')
def main_page():
    return "hello", 200 


app.run(port=5000, host='0.0.0.0')

