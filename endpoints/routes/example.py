import logging
import json
from pymongo import MongoClient

from flask import request, jsonify

from endpoints import app

logger = logging.getLogger(__name__)


@app.route('/example', methods=['GET'])
def example():
    client = pymongo.MongoClient("mongodb+srv://MdAbdullahAlMahin:"+os.getenv('ATLAS_PASS')+"@cluster0.7nvntxs.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
    db = client.testDB
    return jsonify(output)
