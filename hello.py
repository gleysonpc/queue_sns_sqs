import json
import os


def run(event, context):
    print('######## hello ########')
    print({
        'arn': os.environ['NEW_USERS_TOPIC_ARN'],
        'topic': os.environ['NEW_USERS_TOPIC']
    })
    return {"statusCode": 200, "body": json.dumps({'message': 'hi there!'})}
