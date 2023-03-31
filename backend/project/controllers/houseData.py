from flask import Flask, Response, request, Blueprint
from database import db
import json
from bson.objectid import ObjectId
import csv
import sys
sys.path.append("../../../..")
sys.path.append("..")

module_one =  __import__('1-scraper.helperFunc.columnNames')
column_names = module_one.helperFunc.columnNames.column_names

houseData_bp = Blueprint('houseData', __name__)

@houseData_bp.route('/test', methods=['POST'])
def test():
    print("Test")
    print(request.json)
    print(request.json.get('a'))

    return Response(
        response=json.dumps({
            "message":"Test pass"
        }),
        status=200,
        mimetype='application/json'
    )

@houseData_bp.route('/createHouseData', methods=['POST'])
def createHouseData():
    try:
        print(request.json['address'])
        # TODO: can later add the whole column_name here
        houseData = {
            "address": request.json.get('address'),
            "price" : request.json.get('price'),
            "gross_tax": request.json.get('gross_tax'),
        }
        dbResponse = db.houseData.insert_one(houseData)
        print(dbResponse.inserted_id)
        for attr in dir(dbResponse.inserted_id):
            print(attr)
        return Response(
            response=json.dumps({
                "message":"houseData created successfully",
                'id':f'{dbResponse.inserted_id}',
            }),
            status=200,
            mimetype='application/json'
        )

    except Exception as ex:
        print('ERROR - Cannot create user')
        print(ex)

@houseData_bp.route('/renderDataIntoHouseData', methods=['POST'])
def renderDataIntoHouseData():
    #TODO change this to relative path
    csvfile = open('/Users/chiashenglin/Documents/Coding/priceProject/Real-Estate-Predictor-V2/1-scraper/house_data.csv', 'r')
    reader = csv.DictReader( csvfile )
    try:
        modified_row_count = 0
        for each_house_data in reader:
            row={}
            for column_name in column_names:
                #print(field)
                row[column_name]=each_house_data[column_name]

            dbResponse = db.houseData.update(
                {'address': each_house_data['address'] }, 
                {"$set": row},
                upsert = True
            )
            #TODO row count is not correct
            if dbResponse['nModified'] == 1: modified_row_count+=1
        return Response(
            response=json.dumps({
                "message":"successfully render house data",
                "modified_row_count":modified_row_count
            }),
            status=200,
            mimetype='application/json'
        )
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({
                "message":"cannot render house data",
            }),
            status=500,
            mimetype='application/json'
        )
