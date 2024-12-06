import os
import logging
from typing import Optional

from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)

logging.basicConfig(
    filename="./customer_service.log",
    level=logging.ERROR,
    format='%(asctime)s - %(name)s %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)
#  Store the Customer data in MongoDb
client = MongoClient("mongodb://localhost:27017/")
db = client[os.getenv("dataBaseName",False)]
customer_collection = db[os.getenv("collectionName",False)]
if not (os.getenv("dataBaseName",False) or os.getenv("collectionName",False)):
    logger.info(f"provide the missing details db : {db} customer_collection: {customer_collection}")
else:
    logger.info(f"Good to Go db : {db} customer_collection: {customer_collection}")

# Required Routes
# POST /customers: Add a new customer.
@app.route("/customer", methods=["POST"])
def add_customer():
    data = request.get_json()
    result = customer_collection.insert_one(data)
    return jsonify({"message": "Customer added", "id":str(result.inserted_id)}), 201

# GET /customers/<id>: Get a customer by ID.
# PUT /customers/<id>: Update customer data.
# DELETE /customers/<id>: Delete a customer.
@app.route("/customer/<string:id>", methods=["GET", "PUT","DELETE"])
def customer(id):
    if request.method == "GET":
        customer = customer_collection.find_one({"_id": ObjectId(id)})
        if customer:
            customer['_id'] = str(customer["_id"])
            return jsonify(customer)
    elif request.method == "PUT":
        return {"message": "under Development"}
    elif request.method == "DELETE":
        return {"message": "under Development"}








@app.route("/<string:name>",methods=["GET","POST"])
def greetings(name):
    if request.method == "GET":
        return {
            "message": f"Hi {name}"
        }
    else:
        return {
            "message": f"Route not in use"
        }

if __name__ == "__main__":
    app.run(debug=True)