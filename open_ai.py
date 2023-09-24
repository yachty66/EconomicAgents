import openai
import logging 

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class OpenAI:
    def __init__(self, key, model, temperature=0.0):
        openai.api_key = key
        self.model = model
        self.temperature = temperature

    def generate(self, prompt):
        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
        )
        result = response.choices[0]['message']['content']
        return result