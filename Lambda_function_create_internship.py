# create_internship.py
import json, time, uuid
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
    # POST /internships
    try:
        body = json.loads(event.get('body') or "{}")
    except Exception:
        return {"statusCode":400,"headers":CORS_HEADERS,"body":json.dumps({"error":"invalid JSON"})}

    title = (body.get('title') or '').strip()
    if not title:
        return {"statusCode":400,"headers":CORS_HEADERS,"body":json.dumps({"error":"title required"})}

    internship_id = str(uuid.uuid4())
    item = {
        "internshipId": internship_id,
        "title": title,
        "requiredSkills": body.get('requiredSkills', []),
        "company": body.get('company',''),
        "location": body.get('location',''),
        "description": body.get('description',''),
        "duration": body.get('duration',''),
        "postedAt": int(time.time())
    }
    try:
        table.put_item(Item=item)
    except Exception as e:
        return {"statusCode":500,"headers":CORS_HEADERS,"body":json.dumps({"error":"dynamodb error","detail":str(e)})}

    return {"statusCode":201,"headers":CORS_HEADERS,"body":json.dumps(item, default=decimal_default)}
