import requests
import json


def send_message(message):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": "Bearer YOUR_API_KEY",
        "Content-Type": "application/json"
    }
    payload = {
        "messages": [
            {"role": "system", "content": "You are ChatGPT, a large language model."},
            {"role": "user", "content": message}
        ]
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    reply = data["choices"][0]["message"]["content"]

    return reply


# Example usage
user_input = input("Enter your message: ")
response = send_message(user_input)
print("ChatGPT: " + response)