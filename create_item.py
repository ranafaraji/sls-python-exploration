import email
import json
import boto3
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


DYNAMODB = boto3.resource("dynamodb", "us-east-1")
USER_TABLE = DYNAMODB.Table("usersTable")


def hello(event, context):
    
    logger.info(event)
    payload_var = json.loads(event["body"])
    # logger.info(payload_var)
    # logger.info(type(payload_var))

    email_var = payload_var['email']
    name_var = payload_var['name']
    comment_var = payload_var['comment']

    USER_TABLE.put_item(Item= {'pk': email_var ,'name':  name_var, 'user_comment': comment_var})

    body = {
        "message": "Item created successfully.",
    }
    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

