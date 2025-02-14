import services as controller
from flask import Flask, request
from utils.object_message import get_object_message, replace_start
from enums.values_enum import VALUE_ENUM

app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    # Welcome route to confirm the server is running.
    # Returns:
    #     str: Welcome message.
    
    return 'Whatsapp Server'

@app.route('/webhook', methods=['GET'])
def validation_token():
    # Validate the webhook token from WhatsApp.
    # Returns:
    #     str: Challenge string if validation is successful, otherwise error message.

    try:
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        if token == VALUE_ENUM.TOKEN.value and challenge is not None:
            return challenge
        else:
            return 'incorrect token', 403
    except Exception as e:
        return str(e), 403
    
@app.route('/webhook', methods=['POST'])
def get_messages():
    # Process incoming messages from the webhook.
    # Returns:
    #     str: Status message indicating whether the message was sent.
    
    try:
        body = request.get_json()
        entry = body['entry'][0]
        changes = entry['changes'][0]
        value = changes['value']
        contacts = value['contacts'][0]

        name = contacts['profile']['name']
        message = value['messages'][0]
        messageId = message['id']

        text = get_object_message(message)
        number = replace_start(message['from'])

        controller.chatbot(
            name,
            text,
            number,
            messageId,
        )
        return 'sent'

    except Exception as e:
        return 'not sent ' + str(e)
