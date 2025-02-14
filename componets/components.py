import json
from enums.values_enum import VALUE_ENUM

def text_message(number, text):
    # Create a text message payload.
    # Args:
    #     number (str): Recipient's phone number.
    #     text (str): Message body.
    # Returns:
    #     str: JSON-formatted message data.

    data = json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": number,
        "type": "text",
        "text": {
            "body": text
        }
    })
    return data

def button_reply_message(
    number,
    options,
    body,
    footer,
    sedd,
    message_id
):
    # Create a button reply message payload.
    # Args:
    #     number (str): Recipient's phone number.
    #     options (list): List of button options.
    #     body (str): Message body.
    #     footer (str): Message footer.
    #     sedd (str): Session identifier.
    #     message_id (str): Message ID.
    # Returns:
    #     str: JSON-formatted message data.

    buttons = []
    for i, option in enumerate(options):
        buttons.append(
            {
                "type": "reply",
                "reply": {
                    "id": sedd + "_btn_" + str(i + 1),
                    "title": option
                }
            }
        )

    data = json.dumps(
        {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {
                    "text": body
                },
                "footer": {
                    "text": footer
                },
                "action": {
                    "buttons": buttons
                }
            }
        }
    )
    return data

def list_reply_message(
    body,
    sedd,
    footer,
    number,
    options,
    message_id
):
    # Create a list reply message payload.
    # Args:
    #     body (str): Message body.
    #     sedd (str): Session identifier.
    #     footer (str): Message footer.
    #     number (str): Recipient's phone number.
    #     options (list): List of options.
    #     message_id (str): Message ID.
    # Returns:
    #     str: JSON-formatted message data.

    rows = []
    for i, option in enumerate(options):
        rows.append({
            "id": sedd + "_row_" + str(i + 1),
            "title": option,
            "description": ""
        })

    data = json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": number,
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {
                "text": body
            },
            "footer": {
                "text": footer
            },
            "action": {
                "button": "View Options",
                "sections": [
                    {
                        "title": "Sections",
                        "rows": rows
                    }
                ]
            }
        }
    })
    return data

def document_message(
    url,
    number,
    caption,
    filename
):
    # Create a document message payload.
    # Args:
    #     url (str): URL of the document.
    #     number (str): Recipient's phone number.
    #     caption (str): Document caption.
    #     filename (str): Document filename.
    # Returns:
    #     str: JSON-formatted message data.

    data = json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": number,
        "type": "document",
        "document": {
            "link": url,
            "caption": caption,
            "filename": filename
        }
    })
    return data

def sticker_message(number, sticker_id):
    # Create a sticker message payload.
    # Args:
    #     number (str): Recipient's phone number.
    #     sticker_id (str): ID of the sticker.
    # Returns:
    #     str: JSON-formatted message data.

    data = json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": number,
        "type": "sticker",
        "sticker": {
            "id": sticker_id
        }
    })
    return data

def reply_reaction_message(number, message_id, emoji):
    # Create a reaction message payload.
    # Args:
    #     number (str): Recipient's phone number.
    #     message_id (str): Message ID to react to.
    #     emoji (str): Emoji for the reaction.
    # Returns:
    #     str: JSON-formatted message data.
    
    data = json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": number,
        "type": "reaction",
        "reaction": {
            "message_id": message_id,
            "emoji": emoji
        }
    })
    return data

def reply_text_message(number, message_id, text):
    # Create a reply text message payload.
    # Args:
    #     number (str): Recipient's phone number.
    #     message_id (str): Message ID to reply to.
    #     text (str): Reply text.
    # Returns:
    #     str: JSON-formatted message data.
    
    data = json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": number,
        "context": {"message_id": message_id},
        "type": "text",
        "text": {
            "body": text
        }
    })
    return data

def mark_read_message(message_id):
    # Create a payload to mark a message as read.
    # Args:
    #     message_id (str): ID of the message to mark as read.
    # Returns:
    #     str: JSON-formatted message data.

    data = json.dumps({
        "messaging_product": "whatsapp",
        "status": "read",
        "message_id": message_id
    })
    return data
