from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys

import requests
from invokes import invoke_http

# import amqp_setup
# import pika
import json

app = Flask(__name__)
CORS(app)

@app.route("/buy_voucher/<int>:UID/<int:Cost>", methods=['GET'])
def buy_voucher(UID, Cost):
    
    if request.is_json:
        try:
            newVoucher = createNewVoucher()
            newBalance = currentBalance(UID) - Cost
            updateNewBalance = updateUserBalance(UID) 
            
            
        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({
                "code": 500,
                "message": "buyVoucher.py internal error: " + ex_str
            }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400

def createNewVoucher():
    url = "http://localhost:5002/purchasedvoucher/" 
    newVoucher = invoke_http(url, method='POST')
    return newVoucher

def currentBalance(UID):
    url = "http://localhost:5003/user/" + str(UID)
    user = invoke_http(url, method='GET')
    return user['data']['Points']

def updateUserBalance(UID):
    url = "http://localhost:5003/point/" + str(UID)
    updatedBalance = invoke_http(url, method='PUT')
    return updatedBalance

def returnPurchasedVoucher(UID):
    url = "http://localhost:5002/purchasedvoucher/" + str(UID) 
    purchasedVoucher = invoke_http(url, method='GET')
    return purchasedVoucher


if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for placing an order...")
    app.run(host="0.0.0.0", port=6001, debug=True)
    # Notes for the parameters: 
    # - debug=True will reload the program automatically if a change is detected;
    #   -- it in fact starts two instances of the same flask program, and uses one of the instances to monitor the program changes;
    # - host="0.0.0.0" allows the flask program to accept requests sent from any IP/host (in addition to localhost),
    #   -- i.e., it gives permissions to hosts with any IP to access the flask program,
    #   -- as long as the hosts can already reach the machine running the flask program along the network;
    #   -- it doesn't mean to use http://0.0.0.0 to access the flask program.
