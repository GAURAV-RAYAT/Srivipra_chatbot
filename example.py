from flask import Flask
from threading import Thread
app = Flask(__name__)
@app.route('/')

def index():
     print("Chatbot deployed succesfully")
     return "Chatbot deployed succesfully"

def run():
     app.run(host='0.0.0.0',port=8080)
     
def example():
 t = Thread(target=run)
 t.start()