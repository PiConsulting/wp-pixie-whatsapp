import os
from enum import Enum

class ValueEnum(Enum):
    TOKEN = os.getenv('FACEBOOK_TOKEN')
    GRAPH_URL = os.getenv('GRAPH_URL')
    DOCUMENT_PDF = os.getenv('DOCUMENT_PDF')

VALUE_ENUM = ValueEnum