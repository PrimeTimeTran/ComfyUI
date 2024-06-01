import requests
import json


def prompt():
    json_file = "./data.json"
    with open(json_file, 'r') as file:
        json_data = json.load(file)

    api_url = "http://127.0.0.1:8188/prompt"
    response = requests.post(api_url, json=json_data)
    if response.status_code == 200:
        response_data = response.json()

        with open("output.json", 'w') as output_file:
            json.dump(response_data, output_file, indent=4)

        print("Output written to output.json")
    else:
        print(
            f"Failed to make POST request. Status code: {response.status_code}")


if __name__ == "__main__":
    prompt()


# curl -X POST --data api.json http://127.0.0.1:8188/prompt
