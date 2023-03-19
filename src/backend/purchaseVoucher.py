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

@app.route("/validate_voucher/<int:UID>", methods=['GET'])
def validate_voucher(UID):
    # Making sure that vouchers displayed to user are those that they have sufficient points for
    points = getUserPoints(UID)
    vouchers = getVouchers()
    voucherList = getAvailableVouchers(points, vouchers)
    return voucherList

def getUserPoints(UID):
    url = "http://localhost:5003/user/" + str(UID)
    getUser = invoke_http(url, method='GET')
    return str(getUser["data"]["Points"])
    
def getVouchers():
    url = "http://localhost:5001/availablevoucher"
    getVouchers = invoke_http(url, method='GET')
    return getVouchers['data']['AllVouchers']

def getAvailableVouchers(points, vouchers):
    available_vouchers = []
    unavailable_vouchers = []
    total = []
    for voucher in vouchers:
        # return voucher
        if int(voucher['Cost']) < int(points):
            available_vouchers.append(voucher)
        else:
            unavailable_vouchers.append(voucher)
    total.append(available_vouchers)
    total.append(unavailable_vouchers)
    return total

@app.route("/purchase_voucher/<int>:UID/<str:PlatformName>/<str:DiscountAmt>/<int:Cost>", methods=['GET'])
def purchase_voucher(UID, PlatformName, DiscountAmt, Cost):
    
    

# def userBuyVoucher():
#     url = "http://localhost:5002/purchasedvoucher"
#     userBuyVoucher = invoke_http(url, method='POST')
#     return userBuyVoucher
    


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
