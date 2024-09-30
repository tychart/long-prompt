import os
import re
import time
# import pyautogui
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-software-rasterizer")

# Initialize the WebDriver with the options
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://copilot.microsoft.com")

# Load environment variables from .env file
load_dotenv()

# Get the username and password from environment variables
email = os.getenv('EMAIL')
org_password = os.getenv('PASSWORD')

screenshot_counter = 1

def send_long_text(long_text):
    try:
      
        authenticate()

        shadow_tree = {
            "cib_serp": {
                "host": None,
                "root": None,
                "children": {
                    "cib_action_bar": {
                        "host": None,
                        "root": None,
                        "children": {
                            "cib_text_input": {
                                "host": None,
                                "root": None
                            }
                        }
                    },
                    "cib_conversation": {
                        "host": None,
                        "root": None
                    }
                }
            }
        }

        

        # Step 7: Ensure you are back on the original page
        shadow_tree["cib_serp"]["host"] = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "cib-serp"))
        )
        screenshot()
        print("Back To Copilot!")
        shadow_tree["cib_serp"]["root"] = driver.execute_script('return arguments[0].shadowRoot', shadow_tree["cib_serp"]["host"])


        shadow_tree["cib_serp"]["children"]["cib_action_bar"]["host"] = shadow_tree["cib_serp"]["root"].find_element(By.CSS_SELECTOR, "cib-action-bar")
        shadow_tree["cib_serp"]["children"]["cib_action_bar"]["root"] = driver.execute_script('return arguments[0].shadowRoot', shadow_tree["cib_serp"]["children"]["cib_action_bar"]["host"])

        shadow_tree["cib_serp"]["children"]["cib_conversation"]["host"] = shadow_tree["cib_serp"]["root"].find_element(By.CSS_SELECTOR, "cib-conversation")
        shadow_tree["cib_serp"]["children"]["cib_conversation"]["root"] = driver.execute_script('return arguments[0].shadowRoot', shadow_tree["cib_serp"]["children"]["cib_conversation"]["host"])


        shadow_tree["cib_serp"]["children"]["cib_action_bar"]["children"]["cib_text_input"]["host"] = shadow_tree["cib_serp"]["children"]["cib_action_bar"]["root"].find_element(By.CSS_SELECTOR, "cib-text-input")
        shadow_tree["cib_serp"]["children"]["cib_action_bar"]["children"]["cib_text_input"]["root"] = driver.execute_script('return arguments[0].shadowRoot', shadow_tree["cib_serp"]["children"]["cib_action_bar"]["children"]["cib_text_input"]["host"])

        # shadow_host_3_cib_text_input = shadow_root_2_cib_conversation.find_element(By.CSS_SELECTOR, "cib-text-input")
        # shadow_root_3_cib_text_input = driver.execute_script('return arguments[0].shadowRoot', shadow_host_3_cib_text_input)


        text_box = shadow_tree["cib_serp"]["children"]["cib_action_bar"]["children"]["cib_text_input"]["root"].find_element(By.CSS_SELECTOR, "textarea")
        # send_button = shadow_tree["cib_serp"]["children"]["cib_action_bar"]["root"].find_element(By.CSS_SELECTOR, "button[aria-label='Submit']")

        looping_send(shadow_tree, text_box, long_text)

        # time.sleep(100000000)



    except Exception as e:
        # print(f"An error occurred: {e}")
        # print(e)
        raise e
    finally:
        driver.quit()

def authenticate():
    screenshot()
    # Step 1: Click the sign-in button
    shadow_host_1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "cib-serp"))
    )
    shadow_root_1 = driver.execute_script('return arguments[0].shadowRoot', shadow_host_1)
    shadow_host_2 = shadow_root_1.find_element(By.CSS_SELECTOR, "cib-conversation")
    shadow_root_2 = driver.execute_script('return arguments[0].shadowRoot', shadow_host_2)
    shadow_host_3 = shadow_root_2.find_element(By.CSS_SELECTOR, "cib-welcome-container")
    shadow_root_3 = driver.execute_script('return arguments[0].shadowRoot', shadow_host_3)
    button = shadow_root_3.find_element(By.CSS_SELECTOR, "button.muid-cta")
    button.click()

    screenshot()

    # Step 2: Enter email and submit
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "loginfmt"))
    )
    email_input.send_keys(email)
    email_input.send_keys(Keys.RETURN)

    # Step 3: Handle organization login
    org_login_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "passwd"))
    )
    org_login_input.send_keys(org_password)
    org_login_input.send_keys(Keys.RETURN)

    # Step 4: Handle push notification manually (if possible)
    # This step might require manual intervention

    duo_security_key_wait = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "webauthn-request-header"))
    )
    

    # time.sleep(1)
    # screenshot()
    # pyautogui.press('enter')

    # other_options_button = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, ".action-link.other-options-link"))
    # )

    other_options_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".button--link.link.other-options-link"))
    )
    screenshot()

    time.sleep(1)
    other_options_button.click()
    driver.execute_script("arguments[0].click();", other_options_button)
    screenshot()
    # Wait for the element to be present and then click it
    duo_push_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Duo Push')]"))
    )
    screenshot()
    duo_push_button.click()

    

    # Step 5: Handle "Stay signed in" prompt
    duo_stay_signed_in_button = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.ID, "trust-browser-button"))
    )

    screenshot()
    duo_stay_signed_in_button.click()

    # Step 6: Handle "Stay signed in" prompt on microsoft
    microsoft_stay_signed_in_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "idBtn_Back"))
    )
    screenshot()
    microsoft_stay_signed_in_button.click()


def looping_send(shadow_tree, text_box, long_text):
    chunk_list = text_splitter(long_text, 7500)
    chunk_total = len(chunk_list)

    for curr_chunk_count, chunk in enumerate(chunk_list, start=1):
        time.sleep(10)
        text_box.send_keys(chunk)
        print(f"Just output chunk {curr_chunk_count} out of {chunk_total}")

        time.sleep(60 if curr_chunk_count == 1 else 30)
        screenshot()
        text_box.send_keys(Keys.RETURN)

        time.sleep(10)

        wait_typing_indicator_appear(shadow_tree)
        wait_typing_indicator_disappear(shadow_tree)

        time.sleep(10)

        write_responses(shadow_tree, -1)
            
    time.sleep(10)

    # Final update of the output file
    write_responses(shadow_tree)


def wait_typing_indicator_appear(shadow_tree):
    # Wait for cib-typing-indicator to appear within shadow_root_2
    WebDriverWait(shadow_tree["cib_serp"]["children"]["cib_action_bar"]["root"], 1000).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'cib-typing-indicator[visible=""]'))
    )
    print("Typing indicator appeared")

def wait_typing_indicator_disappear(shadow_tree):
    # Wait for cib-typing-indicator to disappear within shadow_root_2
    WebDriverWait(shadow_tree["cib_serp"]["children"]["cib_action_bar"]["root"], 1000).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, 'cib-typing-indicator[visible=""]'))
    )
    print("Typing indicator disappeared")

def write_responses(shadow_tree, response_number=None):
    try:
        chat_turns = shadow_tree["cib_serp"]["children"]["cib_conversation"]["root"].find_elements(By.CSS_SELECTOR, "cib-chat-turn")

        if (response_number == -1):
            if (len(chat_turns) >= 1):
                second_to_latest_conversation = chat_turns[-1]

                shadow_root_conversation = driver.execute_script('return arguments[0].shadowRoot', second_to_latest_conversation)
                
                screenshot()
                # Get the inner HTML of the shadow root
                # shadow_root_html = driver.execute_script("return arguments[0].innerHTML;", shadow_root_conversation)
                # print(shadow_root_html)
                
                shadow_host_cib_message_group = shadow_root_conversation.find_element(By.CSS_SELECTOR, "cib-message-group[source='bot']")
                shadow_root_cib_message_group = driver.execute_script('return arguments[0].shadowRoot', shadow_host_cib_message_group)

                copilot_response = shadow_root_cib_message_group.find_element(By.CSS_SELECTOR, "cib-message")
                response_text = copilot_response.get_attribute("aria-label")

                write_to_file(response_text)
        if (response_number == None):
            # Delete whatever is in the file currently
            print("Writing the complete output file now")
            clear_file()
            for chat_turn in chat_turns:
                shadow_root_conversation = driver.execute_script('return arguments[0].shadowRoot', chat_turn)

                shadow_host_cib_message_group = shadow_root_conversation.find_element(By.CSS_SELECTOR, "cib-message-group[source='bot']")
                shadow_root_cib_message_group = driver.execute_script('return arguments[0].shadowRoot', shadow_host_cib_message_group)

                copilot_response = shadow_root_cib_message_group.find_element(By.CSS_SELECTOR, "cib-message")
                response_text = copilot_response.get_attribute("aria-label")

                write_to_file(response_text)
    except Exception as e:
        print(f"Ran into an error when trying to get and write responses: {e}")

def split_text_simple(text, chunk_size):
    """Splits the text into chunks of specified size and returns a list of chunks."""
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]


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

def read_file_contents(filename):
    """Reads the contents of a text file and returns it as a string."""
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def write_to_file(text, filename="out.md", overwrite=False):
    mode = "w" if overwrite else "a"
    with open(filename, mode, encoding="utf-8") as file:
        file.write(text + "\n")

def clear_file(filename="out.md", backup=False):
    if backup:
        # Create the history directory if it doesn't exist
        history_dir = "history"
        if not os.path.exists(history_dir):
            os.makedirs(history_dir)

        # Extract the base name and extension
        base_name, extension = os.path.splitext(filename)

        # Find the next available backup number
        backup_number = 1
        backup_filename = os.path.join(history_dir, f"{base_name}-backup-{backup_number}{extension}")
        while os.path.exists(backup_filename):
            backup_number += 1
            backup_filename = os.path.join(history_dir, f"{base_name}-backup-{backup_number}{extension}")

        # Read the contents of the current file
        with open(filename, "r", encoding="utf-8") as original_file:
            content = original_file.read()

        # Write the contents to the backup file
        with open(backup_filename, "w", encoding="utf-8") as backup_file:
            backup_file.write(content)

    # Clear the old file
    open(filename, "w").close()

def screenshot(screenshot_dir="screenshots"):
    global screenshot_counter
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    driver.save_screenshot(f'{screenshot_dir}/screenshot{screenshot_counter}.png')
    screenshot_counter += 1



long_text = read_file_contents("in.txt")
send_long_text(long_text)

# Backup the output file just made
clear_file(backup=True)

print("Program Finished! Check the history folder for the final output")
