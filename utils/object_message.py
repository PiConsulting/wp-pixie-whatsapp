def get_object_message(message):
    # Extract the text from the message object based on its type.
    # Args:
    #     message (dict): Message object.
    # Returns:
    #     str: Extracted text.

    if 'type' not in message:
        return 'unrecognized message'

    typeMessage = message['type']
    if typeMessage == 'text':
        text = message['text']['body']
    elif typeMessage == 'button':
        text = message['button']['text']
    elif typeMessage == 'interactive' and message['interactive']['type'] == 'list_reply':
        text = message['interactive']['list_reply']['title']
    elif typeMessage == 'interactive' and message['interactive']['type'] == 'button_reply':
        text = message['interactive']['button_reply']['title']
    else:
        text = 'unprocessed message'
    return text

def replace_start(s):
    # Replace the starting part of the number based on specific prefixes.
    # Args:
    #     s (str): Original number string.
    # Returns:
    #     str: Modified number string.

    number = s[3:]
    if s.startswith("521"):
        return "52" + number
    elif s.startswith("549"):
        return "54" + number
    else:
        return s