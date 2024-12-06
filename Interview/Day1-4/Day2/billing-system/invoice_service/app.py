import os
import logging
import redis
import logging

from  flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

logging.basicConfig(
    filename="./invoice_service.log",
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)
redish_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

#mockdata
invoices = {
    "1":{"id":1, "customer_id":123, "amount":100.0, "status":"paid"},
    "2":{"id":1, "customer_id":456, "amount":200.0, "status":"pending"},
}

@app.route("/<string:name>", methods=["GET"])
def greetings(name):
    logger.error(f" Name: {name}")
    return jsonify({"message":f"Hi {name}"}), 200

# GET: Fetch an invoice
@app.route("/invoices/<string:id>", methods = ["GET"])
def get_invoice(id):
    #check cache
    cached_invoice = redish_client.get(f"invoice:{id}")
    if cached_invoice:
        return jsonify({"source":"cache", "invoice":eval(cached_invoice)})

    #Fetched from Mockdata
    invoice = invoices.get("id")
    if invoice:
        redish_client.setex(f"invoice:{id}", 3600, str(invoice))
        return jsonify({"source":"database","invoice":invoice})
    return jsonify({"error": "Invoice not found"}), 404


if __name__ =="__main__":
    app.run(debug=True,port=5001)