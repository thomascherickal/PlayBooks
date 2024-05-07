import logging

from openai import OpenAI

logger = logging.getLogger(__name__)


class OpenAiApiProcessor:
    client = None

    def __init__(self, open_ai_api_key):
        self.__open_ai_api_key = open_ai_api_key
        self.client = OpenAI(api_key=open_ai_api_key)

    def chat_completions_create(self, model, response_format, messages):
        try:
            response = self.client.chat.completions.create(
                model=model,
                response_format=response_format,
                messages=messages
            )
            return response
        except Exception as e:
            logger.error(f"Exception occurred while exceuting open ai creating chat completions with error: {e}")
        return None
