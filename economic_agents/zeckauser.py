from .open_ai import OpenAI
import matplotlib.pyplot as plt
import numpy as np
import logging 

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Zeckauser:
    def __init__(self, api_key, model, image_path):
        openai_api_key: str = None
        self.openai_api_key = openai_api_key
        self.model = OpenAI(key=api_key, model=model)
        self.image_path = image_path

    def play(self):
        self.base_prompt = """The National Highway Safety Commission is deciding how to allocate its budget between two safety research programs: i) improving automobile safety (bumpers, body, gas tank configurations, seatbelts) and ii) improving the safety of interstate highways (guard rails, grading, highway interchanges, and implementing selective reduced speed limits)."""
        self.ask = f"Please choose your most preferred option in light of your views {[header[h] for h in range(len(options))]}:"
        pass

    def create_plot(self, results):
        pass

    def __call__(self):
        results = self.play()
        self.create_plot(results)
        return results