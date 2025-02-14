from enum import Enum

class OptionsEnum(Enum):
    QUESTION = 'question'
    ACTION = 'action'
    START = 'start'
    MESSAGE = 'message'
    OPENAI = 'openai'

OPTIONS_ENUM = OptionsEnum