import json
import boto3
from decimal import Decimal

REGION = 'ap-south-1'
dynamodb = boto3.resource('dynamodb', region_name=REGION)

# CORS headers used everywhere (change '*' to your S3 origin when ready)
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

# match_for_user handler
profiles_table = dynamodb.Table('Profiles')
intern_table = dynamodb.Table('Internships')

def lambda_handler(event, context):
    # get path parameter
    userId = event.get('pathParameters', {}).get('userId')
    if not userId:
        return {"statusCode":400,"headers":CORS_HEADERS,"body":json.dumps({"error":"userId required"})}

    try:
        resp = profiles_table.get_item(Key={'userId': userId})
        p = resp.get('Item')
        if not p:
            return {"statusCode":404,"headers":CORS_HEADERS,"body":json.dumps({"error":"profile not found"})}

        user_skills = set([s.strip().lower() for s in (p.get('skills') or [])])
        interns_resp = intern_table.scan()
        interns = interns_resp.get('Items', [])
    except Exception as e:
        # return the error for debugging (remove detail in production)
        return {"statusCode":500,"headers":CORS_HEADERS,"body":json.dumps({"error":"dynamodb error","detail":str(e)})}

    results = []
    for it in interns:
        req = [s.strip().lower() for s in (it.get('requiredSkills') or [])]
        matched = sorted(list(user_skills.intersection(req)))
        score = 0
        if req:
            score = round((len(matched) / len(req)) * 100)
        results.append({
            "internship": it,
            "matchedSkills": matched,
            "score": score
        })

    results = sorted(results, key=lambda x: x['score'], reverse=True)
    return {"statusCode":200,"headers":CORS_HEADERS,"body":json.dumps(results, default=decimal_default)}
