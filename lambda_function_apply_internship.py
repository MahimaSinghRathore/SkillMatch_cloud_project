# apply.py
import json, time, uuid
import boto3
from decimal import Decimal

REGION = 'ap-south-1'
dynamodb = boto3.resource('dynamodb', region_name=REGION)
table = dynamodb.Table('Applications')

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
    # POST /apply
    try:
        body = json.loads(event.get('body') or "{}")
    except Exception:
        return {"statusCode":400,"headers":CORS_HEADERS,"body":json.dumps({"error":"invalid JSON"})}

    userId = body.get('userId')
    internshipId = body.get('internshipId')
    if not userId or not internshipId:
        return {"statusCode":400,"headers":CORS_HEADERS,"body":json.dumps({"error":"userId and internshipId required"})}

    item = {
        "applicationId": str(uuid.uuid4()),
        "userId": userId,
        "internshipId": internshipId,
        "status": "submitted",
        "appliedAt": int(time.time())
    }
    try:
        table.put_item(Item=item)
    except Exception as e:
        return {"statusCode":500,"headers":CORS_HEADERS,"body":json.dumps({"error":"dynamodb error","detail":str(e)})}

    return {"statusCode":201,"headers":CORS_HEADERS,"body":json.dumps(item)}
