get_profile.py

import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
table = dynamodb.Table('Profiles')

# Convert Decimal → int/float so json.dumps works
def decimal_default(obj):
    if isinstance(obj, Decimal):
        # if integer-like, convert to int
        if obj % 1 == 0:
            return int(obj)
        return float(obj)
    raise TypeError

# CORS headers used on every response
CORS_HEADERS = {
    "Content-Type": "application/json",
    # Use '*' for quick testing. For production, replace with:
    # "Access-Control-Allow-Origin": "http://skillmatch-mahima.s3-website.ap-south-1.amazonaws.com"
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "Content-Type,Authorization,X-Amz-Date,X-Api-Key,X-Amz-Security-Token",
    "Access-Control-Allow-Methods": "GET,POST,OPTIONS"
}

def lambda_handler(event, context):
    # For console test: pass userId in body
    # For API Gateway: userId will come from pathParameters
    try:
        userId = event.get('pathParameters', {}).get('userId') or \
                 json.loads(event.get('body') or "{}").get('userId')
    except Exception:
        # malformed JSON body
        return {
            "statusCode": 400,
            "headers": CORS_HEADERS,
            "body": json.dumps({"error": "invalid JSON in body"})
        }

    if not userId:
        return {
            "statusCode": 400,
            "headers": CORS_HEADERS,
            "body": json.dumps({"error": "userId required"})
        }

    try:
        resp = table.get_item(Key={'userId': userId})
    except Exception as e:
        # DynamoDB error
        return {
            "statusCode": 500,
            "headers": CORS_HEADERS,
            "body": json.dumps({"error": "internal error", "detail": str(e)})
        }

    if 'Item' not in resp:
        return {
            "statusCode": 404,
            "headers": CORS_HEADERS,
            "body": json.dumps({"error": "not found"})
        }

    # Return the profile with Decimal fixed
    return {
        "statusCode": 200,
        "headers": CORS_HEADERS,
        "body": json.dumps(resp['Item'], default=decimal_default)
    }
