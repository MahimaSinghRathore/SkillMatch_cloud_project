# list_internships.py
import json
import boto3
from decimal import Decimal

REGION = 'ap-south-1'
dynamodb = boto3.resource('dynamodb', region_name=REGION)
table = dynamodb.Table('Internships')

CORS_HEADERS = {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "Content-Type,Authorization,X-Amz-Date,X-Api-Key,X-Amz-Security-Token",
    "Access-Control-Allow-Methods": "GET,POST,OPTIONS"
}

def decimal_default(obj):
    if isinstance(obj, Decimal):
        if obj % 1 == 0:
            return int(obj)
        return float(obj)
    raise TypeError

def lambda_handler(event, context):
    # GET /internships
    try:
        resp = table.scan()
        items = resp.get('Items', [])
    except Exception as e:
        return {"statusCode":500,"headers":CORS_HEADERS,"body":json.dumps({"error":"dynamodb error","detail":str(e)})}

    return {"statusCode":200,"headers":CORS_HEADERS,"body":json.dumps(items, default=decimal_default)}
