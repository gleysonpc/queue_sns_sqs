import json
from user_model import create_user


def run(event, context):
    print('######## process_new_users ########')
    
    for record in event.get('Records'):
        body = json.loads(record.get('body'))
        message = json.loads(body.get('Message'))
        name = message.get('name')
        create_user(name)

    return {"statusCode": 200, "body": {}}
