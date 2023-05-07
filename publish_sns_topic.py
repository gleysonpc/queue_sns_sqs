import boto3


def publish_message_sns(topic_arn, message):
    """
    Publica uma mensagem em um tópico do Amazon SNS.

    :param topic_arn: O ARN (Amazon Resource Name) do tópico do SNS.
    :param message: A mensagem que será publicada no tópico.
    """

    # Cria um objeto do cliente SNS
    sns_client = boto3.client('sns')

    # Publica a mensagem no tópico
    response = sns_client.publish(
        TopicArn=topic_arn,
        Message=message
    )

    # Imprime a resposta da publicação da mensagem
    print(response)


# Chama a função para publicar a mensagem no tópico do SNS
# publish_message_sns(
#     'arn:aws:sns:us-east-1:123456789012:my-topic',
#     'Minha mensagem de teste'
# )
