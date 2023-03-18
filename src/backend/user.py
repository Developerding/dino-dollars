from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/user'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)  

class User(db.Model):
    __tablename__ = 'USER'
    UID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(64), nullable=False)
    Email = db.Column(db.String(64), nullable=False)
    Points = db.Column(db.Integer, nullable=False)

    def __init__(self, UID, Name, Email, Points):
        self.UID = UID
        self.Name = Name
        self.Email = Email
        self.Points = Points

    def json(self):
        user = {"UID": self.UID, "Name": self.Name, "Email": self.Email, "Points": self.Points}
        user['LinkedAccs'] = []
        for acc in self.ACCOUNTS:
            user['LinkedAccs'].append(acc.json())
        return user


class Accounts(db.Model):
    __tablename__ = 'ACCOUNTS'
    UID = db.Column(db.ForeignKey('USER.UID', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    Name = db.Column(db.String(64), primary_key=True)

    def __init__(self, UID, Name):
        self.UID = UID
        self.Name = Name

    accs = db.relationship(
        'User', primaryjoin='Accounts.UID == User.UID', backref='ACCOUNTS')

    def json(self):
        return {"UID": self.UID, "Name": self.Name}

@app.route('/user', methods=['GET'])
def get_all():
    userList = User.query.all()
    if len(userList):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "users": [user.json() for user in userList]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no users."
        }
    ), 404
@app.route("/user/<int:UID>")
def find_by_UID(UID):
    user = User.query.filter_by(UID=UID).first()
    if user:
        return jsonify(
            {
                "code": 200,
                "data": user.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "User not found."
        }
    ), 404


@app.route("/user/<int:UID>", methods=['POST'])
def create_user(UID):
    if (User.query.filter_by(UID=UID).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "UID": UID
                },
                "message": "User already exists."
            }
        ), 400

    data = request.get_json()
    user = User(UID, **data)

    try:
        db.session.add(user)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "UID": UID
                },
                "message": "An error occurred creating the user."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": user.json()
        }
    ), 201


@app.route("/point/<int:UID>", methods=['PUT'])
def update_user(UID):
    try:
        user = User.query.filter_by(UID=UID).first()
        if not user:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "user": user
                    },
                    "message": "user not found."
                }
            ), 404

        # update status
        data = request.get_json()
        if data['Points']:
            user.Points = data['Points']
            db.session.commit()
            return jsonify(
                {
                    "code": 200,
                    "data": user.json()
                }
            ), 200
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "user": user
                },
                "message": "An error occurred while updating the points. " + str(e)
            }
        ), 500


@app.route("/user/<int:UID>", methods=['DELETE'])
def delete_user(UID):
    user = User.query.filter_by(UID=UID).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "UID": UID
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "UID": UID
            },
            "message": "User not found."
        }
    ), 404

@app.route("/accounts/<int:UID>/<string:Name>", methods=['POST'])
def create_account(UID,Name):
    if (Accounts.query.filter_by(UID=UID, Name=Name).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "UID": UID,
                    "Name": Name
                },
                "message": "User has already linked account."
            }
        ), 400

    data = request.get_json()
    account = Accounts(UID, Name)

    try:
        db.session.add(account)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "UID": UID,
                    "Name": Name
                },
                "message": "An error occurred linking the account."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": account.json()
        }
    ), 201

if __name__ == '__main__':
    app.run(port=5003, debug=True)