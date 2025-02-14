import time
from enums.values_enum import VALUE_ENUM
from enums.options_enum import OPTIONS_ENUM
from utils.send_message import send_message
from componets import components

def send_responses(number, responses):
    # Helper function to send accumulated responses.
    for item in responses:
        send_message(item)

def create_reply_button_message(number, options, body, footer, sedd, message_id):
    # Helper function to create a reply button message.
    return components.button_reply_message(
        number,
        options,
        body,
        footer,
        sedd,
        message_id
    )

def create_list_reply_message(body, sedd, number, footer, options, message_id):
    # Helper function to create a list reply message.
    return components.list_reply_message(
        body=body,
        sedd=sedd,
        number=number,
        footer=footer,
        options=options,
        message_id=message_id
    )

def chatbot(name, text, number, message_id):
    # Main chatbot function that processes messages and responds
    # based on the received text.

    # Args:
    #     name (str): Name of the user.
    #     text (str): Text of the received message.
    #     number (str): User's phone number.
    #     message_id (str): ID of the received message.

    responses = []

    # Convert the text to lowercase for easier comparison.
    text = text.lower()
    responses.append(components.mark_read_message(message_id))

    if OPTIONS_ENUM.QUESTION.value in text:
        # Option 3: Send PDF document
        responses.append(create_reply_button_message(
            number,
            ["Si", "No"],
            "Su dia fue un buen dia?",
            "Pi Consulting",
            "sed3",
            message_id
        ))

    elif OPTIONS_ENUM.ACTION.value in text:
        # Option 4: Send document and schedule meeting
        responses.append(components.text_message(
            number,
            "Gracias!, espere un momento..."
        ))

        send_responses(number, responses)
        time.sleep(3)

        # Clear responses to send the next batch
        responses = [] 
        responses.append(components.document_message(
            number,
            VALUE_ENUM.DOCUMENT_PDF.value,
            "Bien",
            "Se cumplio la accion que esperaba! 👍🏻"
        ))
        send_responses(number, responses)
        time.sleep(3)

        # Clear responses to send the next batch
        responses = [] 
        responses.append(create_reply_button_message(
            number,
            ["Si", "No"],
            "Se cumplio la accion que esperaba!, quiere algo mas?",
            "Pi Consulting",
            "sed4",
            message_id
        ))

    elif OPTIONS_ENUM.START.value in text:
        # Option 6: Select date and time for meeting
        responses.append(create_list_reply_message(
            "Bienvenido al servicio de atencion, si necesita algo aqui dejamos el catalogo de servicios",
            "sed5",
            number,
            "Pi Consulting",
            ["option", "action", "start", "message", "openai"],
            message_id
        ))

    elif OPTIONS_ENUM.MESSAGE.value in text:
        # Option 8: Farewell and free materials
        responses.append(components.text_message(
            number,
            "No se entendio su pregunta."
        ))

    else:
        responses.append(components.text_message(
            number,
            "mensage por defecto"
        ))

    send_responses(number, responses)
