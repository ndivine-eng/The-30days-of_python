from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient

app = Flask(__name__)  # ✅ Correct use of __name__

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["myDatabase"]
collection = db["user"]

# Route to show homepage
@app.route('/')
def home():
    return "Flask is working and connected to MongoDB!"

# Route to show HTML form
@app.route('/form')
def form():
    return render_template('form.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = int(request.form['age'])
    email = request.form['email']
    location = request.form['location']

    user_data = {
        'name': name,
        'age': age,
        'email': email,
        'location': location
    }

    result = collection.insert_one(user_data)

    return f"User {name} added successfully! ID: {str(result.inserted_id)}"

# Optional: API route to submit JSON
@app.route('/add', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    result = collection.insert_one(data)

    return jsonify({
        "message": "Data added successfully",
        "inserted_id": str(result.inserted_id)
    }), 201

# ✅ Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
