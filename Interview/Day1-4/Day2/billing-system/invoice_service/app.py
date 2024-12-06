import os
import logging
from logging import basicConfig

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

@app.route("/<string:name>", methods=["GET"])
def greetings(name):
    logger.error(f" Name: {name}")
    return jsonify({"message":f"Hi {name}"}), 200



if __name__ =="__main__":
    app.run(debug=True)