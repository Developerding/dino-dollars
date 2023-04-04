from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

app = Flask(__name__)
##Rememeber to change db connection using environ
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/availablevoucher'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)  

#creating a AvailableVoucher object 
class AvailableVoucher(db.Model):
    __tablename__ = 'availableVoucher'

    PlatformName = db.Column(db.String(50), nullable=False, primary_key=True)
    DiscountAmt = db.Column(db.Integer, nullable=False, primary_key=True)
    DDRequired=db.Column(db.Integer, nullable=False)

    #init AvailableVoucher object
    def __init__(self, PlatformName, DDRequired, DiscountAmt):
        self.Platform_Name=PlatformName
        self.DiscountAmt=DiscountAmt
        self.DDrequired=DDRequired

    #returned object in JSON format
    def json(self):
        
        return {
            'Platform_Name': self.PlatformName,
            'DiscountAmt': self.DiscountAmt,
            'DDRequired': self.DDRequired
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