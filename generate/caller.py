import requests
import json

with open("./data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

prompt = {"prompt": data}

encoded_prompt = json.dumps(prompt).encode('utf-8')

response = requests.post("http://127.0.0.1:8188/prompt", data=encoded_prompt)
print(response)
