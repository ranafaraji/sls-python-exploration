import email
import json
from unicodedata import name
import boto3
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


DYNAMODB = boto3.resource("dynamodb", "us-east-1")
USER_TABLE = DYNAMODB.Table("usersTable")

def handler(event, context):
    
    logger.info(event)

    payload_var = json.loads(event["body"])
    email_var = payload_var['email']
    name_var = payload_var['name']


    response = USER_TABLE.update_item(
    Key={'pk': email_var},
    UpdateExpression="SET #name_att = :new_name_var",
    ExpressionAttributeNames={'#name_att': 'name'},
    ExpressionAttributeValues={':new_name_var' : name_var},
    ReturnValues="UPDATED_NEW"
    )
    logger.info(response['Attributes'])
    
    response = {"statusCode": 200, "body": json.dumps(response)}

    return response

