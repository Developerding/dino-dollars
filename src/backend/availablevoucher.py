from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

app = Flask(__name__)
##Rememeber to change db connection using environ

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)  

#creating a AvailableVoucher object 
class AvailableVoucher(db.Model):
    __tablename__ = 'AvailableVouchers'

    PlatformName = db.Column(db.String(50), nullable=False, primary_key=True)
    Cost = db.Column(db.Integer, nullable=False)
    DiscountAmt = db.Column(db.String(20), nullable=False, primary_key=True)
    

    #init AvailableVoucher object
    def __init__(self, PlatformName, Cost, DiscountAmt):
        self.Platform_Name=PlatformName
        self.Cost=Cost
        self.DiscountAmt=DiscountAmt

    #returned object in JSON format
    def json(self):
        
        return {
            'Platform_Name': self.PlatformName,
            'Cost': self.Cost,
            'DiscountAmt': self.DiscountAmt
        }
    


#function to access all available vouchers:
@app.route('/availablevoucher', methods=['GET'])
def get_all():
    all_available_voucher_list=AvailableVoucher.query.all()
    if len(all_available_voucher_list):
        return jsonify(
            {
                "code":200,
                "data": {
                    "AllVouchers": [voucher.json() for voucher in all_available_voucher_list]
                }
            }
        )
    
    #else: no available vouchers
    return jsonify(
        {
            'code':410,
            "message": "There are no available vouchers."
        }
    )




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)