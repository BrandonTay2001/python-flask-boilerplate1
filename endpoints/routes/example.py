import logging
import json
from pymongo import MongoClient
# from os import environ
import os

from flask import request, jsonify

from endpoints import app

logger = logging.getLogger(__name__)

from dotenv import load_dotenv
load_dotenv()

@app.route('/example', methods=['GET'])
def example():
    password = os.getenv('ATLAS_PASS')
    client = MongoClient("mongodb+srv://MdAbdullahAlMahin:MvPSCHBVtcW4w8Tx@cluster0.7nvntxs.mongodb.net/?retryWrites=true&w=majority")
    db = client['testDB']
    collection = db['testCol']
    doc_count = collection.count_documents({})
    print(doc_count)
    # return jsonify(doc_count)
    return "hello"