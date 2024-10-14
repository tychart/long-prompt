import requests

# Ollama API endpoint
api_endpoint = 'http://192.168.10.35:11434/api/chat'

messages = []

def send_payload(url, data):

    try:
        # Make a POST request with JSON payload
        response = requests.post(url, json=data)

        # Check if the request was successful
        response.raise_for_status()

        return response
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that occur during the request
        print(f"Request error: {e}")

def add_question(messages, prompt, text):
    message = prompt + "\n\n" + text
    return add_message(messages, "user", message)


def add_message(messages, role, message):
    new_message = {
        "role": role,
        "content": message
    }
    
    messages.append(new_message)
    return messages


def dostuff():
  messages = add_question(messages, "Make this cooler:", "My aunt has 3 bycicles")
  response = send_payload(api_endpoint, messages)

  json_response = response.json()
  returned_message = json_response["message"]["content"]
  print(returned_message)
  messages = add_message(messages, "assistant", returned_message)
  print("fullmessages:")
  print(messages)

dostuff()

# # Read the conversation history from the file
# with open('conversation.txt', 'r') as f:
#     history = [line.strip().split('\t') for line in f]

# # Append the new prompt to the history
# history.append(['What is the capital of France?', ''])

# Create the API request payload
# payload = {
#     # 'prompt': history,
#     "model": "llama3.2",
#     'prompt': "This is a test right now",
#     'temperature': 0.8
# }

#history = "Tell me everything you know about waterbottles"

# messages = [
#     {
#       "role": "user",
#       "content": "what color is the sky?"
#     },
#     {
#       "role": "assistant",
#       "content": "the sky is usualy blue"
#     },
#     {
#       "role": "user",
#       "content": "why?"
#     },
#     {
#       "role": "assistant",
#       "content": """The reason why the sky appears blue is due to a phenomenon called Rayleigh scattering, named after the British physicist Lord Rayleigh, who first described it in the late 19th century.

# Here's what happens:

# 1. When sunlight enters Earth's atmosphere, it encounters tiny molecules of gases such as nitrogen (N2) and oxygen (O2).
# 2. These molecules scatter the light in all directions, but they scatter shorter (blue) wavelengths more than longer (red) wavelengths.
# 3. This is because the smaller molecules are more effective at scattering the shorter wavelengths.
# 4. As a result, the blue light is dispersed throughout the atmosphere, giving the sky its blue color.

# It's worth noting that during sunrise and sunset, the sky can take on hues of red, orange, and pink due to a different type of scattering called Mie scattering. This occurs when sunlight passes through atmospheric particles like dust, water vapor, and pollutants, which scatter the longer wavelengths of light (like red and yellow) more than the shorter wavelengths.

# So, in short, the sky appears blue because of the way that tiny molecules in the atmosphere scatter sunlight!"""
#     },
#     {
#       "role": "user",
#       "content": "So what wavelength will that normaly be at then?"
#     }
#   ]

# history.append({"prompt": "What is the capital of France?", "response": ""})

# payload = {
#     "model": "llama3.2",
#     "messages": messages,
#     "stream": False
# }

# # # Send the API request
# # response = requests.post(api_endpoint, json=payload)

# response = send_text(api_endpoint, payload)
# # response = send_text(api_endpoint, prompt="Tell me everything you know about ", text="Waterbottles")


# print(response)
# # Print the API response
#print(response.json()['choices'][0]['text'])