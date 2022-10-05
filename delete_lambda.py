from inspect import Attribute
import json
import boto3
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

DYNAMODB = boto3.resource("dynamodb", "us-east-1")
USER_TABLE = DYNAMODB.Table("usersTable")

def handler(event, content):

    payload_var = json.loads(event["body"])

    del_key = payload_var['delete_key']

    table = DYNAMODB.Table('usersTable')
    response = table.delete_item(
        Key={
            'pk' : del_key
        }
    )
    body = {
        "message": "Item deleted successfully.",
    }
    response = {"statusCode": 200, "body": json.dumps(body)}

    return response


