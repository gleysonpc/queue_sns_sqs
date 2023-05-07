# import json


def run(event, context):

    print('######## users_notify ########')
    for record in event.get('Records'):
        sns = record.get('Sns')
        message = sns.get('Message')
        print(message)

    return {"statusCode": 200, "body": {}}
