from flask import Flask, request, redirect
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
client = MongoClient(os.getenv("MONGO_URI"))
db = client["mydb"]
collection = db["users"]

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']
        collection.insert_one({'name': name, 'email': email})
        return redirect("http://localhost:3000/success")
    except Exception as e:
        return redirect(f"http://localhost:3000/?error={str(e)}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
