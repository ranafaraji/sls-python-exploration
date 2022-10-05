import json
import boto3
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


DYNAMODB = boto3.resource("dynamodb", "us-east-1")
USER_TABLE = DYNAMODB.Table("usersTable")
  

def handler(event, context):

    logger.info(event)

    givenn_pk = event['pathParameters']['front-end']
    get_response=USER_TABLE.get_item(Key={"pk": givenn_pk})
    
    response = {"statusCode": 200, "body": json.dumps(get_response)}

    return response