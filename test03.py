import requests

# Ollama API endpoint
api_endpoint = 'http://192.168.10.35:11434/api/chat'


def send_text(url, data=None, prompt=None, text=None):

    if data is None:
        data = {
            "model": "llama3.2",
            "prompt": prompt + " " + text,
            "stream": False
        }

    try:
        # Make a POST request with JSON payload
        response = requests.post(url, json=data)

        # Check if the request was successful
        response.raise_for_status()

        json_response = response.json()

        print(json_response["message"]["content"])
        return response
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that occur during the request
        print(f"Request error: {e}")






# Read the conversation history from the file
with open('conversation.txt', 'r') as f:
    history = [line.strip().split('\t') for line in f]

# Append the new prompt to the history
history.append(['What is the capital of France?', ''])

# Create the API request payload
payload = {
    # 'prompt': history,
    "model": "llama3.2",
    'prompt': "This is a test right now",
    'temperature': 0.8
}

#history = "Tell me everything you know about waterbottles"

messages = [
    {
      "role": "user",
      "content": "what color is the sky?"
    },
    {
      "role": "assistant",
      "content": "the sky is usualy blue"
    },
    {
      "role": "user",
      "content": "why?"
    }
  ]

# history.append({"prompt": "What is the capital of France?", "response": ""})

payload = {
    "model": "llama3.2",
    "messages": messages,
    "stream": False
}

# # Send the API request
# response = requests.post(api_endpoint, json=payload)

response = send_text(api_endpoint, payload)
# response = send_text(api_endpoint, prompt="Tell me everything you know about ", text="Waterbottles")


print(response)
# Print the API response
#print(response.json()['choices'][0]['text'])