from flask import Blueprint, render_template
from pymongo import MongoClient

# Create the Blueprint instance
api_app = Blueprint('myApp', __name__)

# MongoDB connection (same database as in app.py)
client = MongoClient("mongodb://localhost:27017/")
db = client["myAppDB"]
collection = db["users"]  # Change collection if needed

# Route to render the items from MongoDB
@api_app.route('/items', methods=['GET'])
def items():
    # Fetch all items from the collection
    items = collection.find()  # Fetch all documents in the 'users' collection (change collection if needed)
    
    # Render the items in the 'items.html' template
    return render_template('items.html', items=items)