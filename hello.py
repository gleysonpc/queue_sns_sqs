import json
import os


def run(event, context):
    print('######## hello ########')
    print({
        'arn': os.environ['NEW_USERS_TOPIC_ARN'],
        'db_user': os.environ['DB_USER']
    })
    return {"statusCode": 200, "body": json.dumps({'message': 'hi there!'})}
