import requests
import re
from pprint import pprint
import argparse

# Ollama API endpoint
api_endpoint = 'http://192.168.10.35:11434/api/chat'
api_endpoint_k8s = 'http://10.11.14.221:11434/api/chat'

def send_messages(url, messages):
    payload = build_payload(messages)
    return send_payload(url, payload)

def send_payload(url, data):

    try:
        # Make a POST request with JSON payload
        response = requests.post(url, json=data)

        # Check if the request was successful
        response.raise_for_status()
        response.json()
        return response
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that occur during the request
        print(f"Request error: {e}")

def build_payload(messages, model="llama3.2", stream=False):
    return {
        "model": "llama3.2",
        "messages": messages,
        "stream": False
    }


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


def text_splitter(text, chunk_size):
    """Splits the text into chunks based on sentence boundaries and returns a list."""
    text = re.sub(r'\n', ' ', text)
    sentences = re.split(r'(?<=[.!?]) +', text)
    current_chunk = ""
    chunks = []

    for sentence in sentences:
        if len(current_chunk) + len(sentence) + 1 <= chunk_size:
            current_chunk += sentence + " "
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            if len(sentence) > chunk_size:
                words = sentence.split()
                current_sentence = ""
                for word in words:
                    if len(current_sentence) + len(word) + 1 <= chunk_size:
                        current_sentence += word + " "
                    else:
                        chunks.append(current_sentence.strip())
                        current_sentence = word + " "
                if current_sentence:
                    chunks.append(current_sentence.strip())
            else:
                current_chunk = sentence + " "
    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def looping_send(text_list, prompt):
    curr_chunk = 1
    messages = []

    for chunk in text_list:
        print(f"Working on chunk {curr_chunk} out of {len(text_list)}\n")
        # send_text(url, prompt, chunk)

        messages = add_question(messages, prompt, chunk)
        response = send_messages(api_endpoint, messages)

        json_response = response.json()
        returned_message = json_response["message"]["content"]
        print(returned_message)
        messages = add_message(messages, "assistant", returned_message)

        print(f"\nJust finished chunk {curr_chunk} out of {len(text_list)}")
        curr_chunk += 1
    return messages

def parse_responses(messages):
    out_str = ""
    for message in messages:
        if (message["role"] == "assistant"):
            out_str += "\n\n" + message["content"]
    return out_str

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def write_to_file(text, filename="out.md", overwrite=True):
    mode = "w" if overwrite else "a"
    with open(filename, mode, encoding="utf-8") as file:
        file.write(text + "\n")

def dostuff(text, prompt, out_filename="out.md"):


    text_list = text_splitter(text, 6000)
    messages = looping_send(text_list, prompt)

    pprint(messages)

    responses_str = parse_responses(messages)

    write_to_file(responses_str, out_filename)

def main():
    parser = argparse.ArgumentParser(description="Process a prompt, an input file, and produce an output file.")
    parser.add_argument('prompt', type=str, help="The prompt text")
    parser.add_argument('input_file', type=str, help="Path to the input file")
    parser.add_argument('output_file', type=str, help="Path to the output file")

    args = parser.parse_args()


    # Read the prompt file
    prompt = read_file(args.prompt)

    # Read the content of the input file
    input_text = read_file(args.input_file)


    dostuff(input_text, prompt, args.output_file)


if __name__ == "__main__":
    main()
