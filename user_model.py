import boto3
from uuid import uuid4

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UsersTable-dev')


def generate_uuid():
    return str(uuid4())


def create_user(name: str):
    table.put_item(
        Item={
            'id': generate_uuid(),
            'name': name
        }
    )
