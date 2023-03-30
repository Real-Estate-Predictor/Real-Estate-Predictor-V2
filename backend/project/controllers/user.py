from flask import Flask, Response, request, Blueprint
from database import db
import json
from bson.objectid import ObjectId
import csv
import sys
sys.path.append("../../..")


user_bp = Blueprint('user', __name__)

@user_bp.route('/create_user', methods=['POST'])
def create_user():
    try:
        user = {
            'name':request.form['name'], 
            'lastName':request.form['lastName']
        }
        dbResponse = db.users.insert_one(user)
        for attr in dir(dbResponse.inserted_id):
            print(attr)
        return Response(
            response=json.dumps({
                "message":"user created successfully",
                'id':f'{dbResponse.inserted_id}',
            }),
            status=200,
            mimetype='application/json'
        )
    except Exception as ex:
        print('ERROR - Cannot create user')
        print(ex)

################################
@user_bp.route('/get_user', methods=['GET'])
def get_user():
    try:
        data = list(db.users.find())
        for user in data:
            user['_id'] = str(user['_id'])

        return Response(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({
                "message":"cannot get user",
                
            }),
            status=500,
            mimetype='application/json'
        )
################################
@user_bp.route("/update_user/<id>", methods=['PATCH'])
def update_user(id):
    try:
        dbResponse = db.users.update_one(
            {"_id":ObjectId(id)},
            {"$set":{"name":request.form["name"]}}
        )
        for attr in dir(dbResponse):
            print(f'{attr}')
        
        if (dbResponse.modified_count == 1):
            return Response(
                response=json.dumps({'message':'good'}),
                status=200,
                mimetype='application/json'
            )
        else:
            return Response(
                response=json.dumps({'message':'nothing to update'}),
                status=200,
                mimetype='application/json'
            )
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({
                "message":"cannot update user",
            }),
            status=500,
            mimetype='application/json'
        )
################################
@user_bp.route('/delete_user/<id>', methods=['DELETE'])
def delete_user(id):
    db.users.delete_one({'_id':"Maki"})