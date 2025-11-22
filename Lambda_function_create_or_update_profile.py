import json
import time
import boto3

dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
table = dynamodb.Table('Profiles')

# CORS headers returned on every response (replace "*" with your site origin for production)
CORS_HEADERS = {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "Content-Type,Authorization,X-Amz-Date,X-Api-Key,X-Amz-Security-Token",
    "Access-Control-Allow-Methods": "GET,POST,OPTIONS"
}

def _to_list(value):
    """Normalize skills/interests: accept list or comma-separated string."""
    if value is None:
        return []
    if isinstance(value, list):
        return [str(x).strip() for x in value if str(x).strip()]
    if isinstance(value, str):
        return [s.strip() for s in value.split(",") if s.strip()]
    # fallback - put as single string
    return [str(value).strip()]

def _resp(status, body):
    return {"statusCode": status, "headers": CORS_HEADERS, "body": json.dumps(body)}

def lambda_handler(event, context):
    # Allow quick OPTIONS preflight
    if event.get("httpMethod") == "OPTIONS" or event.get("requestContext", {}).get("http", {}).get("method") == "OPTIONS":
        return {"statusCode": 200, "headers": CORS_HEADERS}

    try:
        raw_body = event.get("body") or "{}"
        # If API Gateway sends body base64-encoded, Lambda proxy will already give decoded body;
        # still safe to try/catch JSON parsing.
        try:
            body = json.loads(raw_body)
        except Exception:
            # sometimes test events pass an already-parsed object
            if isinstance(raw_body, dict):
                body = raw_body
            else:
                return _resp(400, {"error": "invalid JSON in request body"})

        userId = body.get("userId")
        if not userId:
            return _resp(400, {"error": "userId required"})

        # normalize fields
        name = body.get("name", "")
        skills = _to_list(body.get("skills"))
        interests = _to_list(body.get("interests"))
        year = str(body.get("year", "")).strip()
        created_at = int(time.time())

        item = {
            "userId": userId,
            "name": name,
            "skills": skills,
            "interests": interests,
            "year": year,
            "createdAt": created_at
        }

        # write to DynamoDB
        table.put_item(Item=item)

        return _resp(201, item)

    except Exception as e:
        # log to CloudWatch automatically; return safe message
        return _resp(500, {"error": "internal server error", "detail": str(e)})
