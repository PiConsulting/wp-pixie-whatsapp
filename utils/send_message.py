import requests
from enums.values_enum import VALUE_ENUM

def send_message(data):
    # Send a message using the WhatsApp API.
    # Args:
    #     data (str): JSON-formatted message data.
    # Returns:
    #     tuple: Status message and status code.

    try:
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {VALUE_ENUM.TOKEN.value}'
        }
        response = requests.post(
            url=VALUE_ENUM.GRAPH_URL.value,
            headers=headers,
            data=data
        )

        if response.status_code == 200:
            return 'message sent', response.status_code
        else:
            return 'error sending message', response.status_code
    except Exception as e:
        return str(e), 403