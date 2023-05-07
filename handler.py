import json
import os
from publish_sns_topic import publish_message_sns
from user_model import generate_uuid


def run(event, context):
    print('######## app ########')
    body = json.loads(event.get('body'))
    sns_arn = os.environ['NEW_USERS_TOPIC_ARN']
    user = {
        'id': generate_uuid(),
        'name': body.get('name')
    }
    publish_message_sns(sns_arn, json.dumps(user))

    return {"statusCode": 200, "body": json.dumps(body)}
