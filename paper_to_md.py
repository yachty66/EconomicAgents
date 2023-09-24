# pip3 install banana-dev
import banana_dev as client
from dotenv import load_dotenv
import os
load_dotenv()
# Create a reference to your model on Banana
my_model = client.Client(
    api_key=os.getenv('API_KEY_BANANA'),    
    model_key=os.getenv('MODEL_KEY_BANANA'),   
    url=os.getenv('URL_BANANA'),  
)
inputs = {
    "pdf_link": "https://filebin.net/157g6dglpzlpffnu/llm_ask.pdf"
}
result, meta = my_model.call("/", inputs)
with open('output.md', 'w') as f:
    f.write(result["content"])
print(result)