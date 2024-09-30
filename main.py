import os
import re
import time
import pyautogui
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://copilot.microsoft.com")

# Load environment variables from .env file
load_dotenv()

# Get the username and password from environment variables
email = os.getenv('EMAIL')
org_password = os.getenv('PASSWORD')

def send_long_text(long_text):
    try:

        '''      
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
        time.sleep(1)
        pyautogui.press('enter')

        other_options_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".action-link.other-options-link"))
        )
        # other_options_button = duo_security_key_cancled.find_element(By.CSS_SELECTOR, "action-link other-options-link")
        other_options_button.click()

        # Wait for the element to be present and then click it
        duo_push_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Duo Push')]"))
        )
        duo_push_button.click()


        # duo_security_key_wait.send_keys(Keys.RETURN)


        # Step 5: Handle "Stay signed in" prompt
        duo_stay_signed_in_button = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.ID, "trust-browser-button"))
        )

        # print(f"Found trust browser button! {duo_stay_signed_in_button.text}")
        duo_stay_signed_in_button.click()


        # Step 6: Handle "Stay signed in" prompt on microsoft
        microsoft_stay_signed_in_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "idBtn_Back"))
        )
        microsoft_stay_signed_in_button.click()
'''
        

        # Step 6: Ensure you are back on the original page
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.CLASS_NAME, "b_wlcmDesc")) # Just the heading text of Copilot
        # )

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
        shadow_tree["cib_serp"]["host"] = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "cib-serp"))
        )
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
        send_button = shadow_tree["cib_serp"]["children"]["cib_action_bar"]["root"].find_element(By.CSS_SELECTOR, "button[aria-label='Submit']")

        looping_send(
            shadow_tree,
            text_box, 
            long_text
        )

        # time.sleep(100000000)



    except Exception as e:
        print(f"An error occurred: {e}")
        print(e)
        raise e
    finally:
        driver.quit()

def authenticate():
            
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
    time.sleep(1)
    pyautogui.press('enter')

    other_options_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".action-link.other-options-link"))
    )
    # other_options_button = duo_security_key_cancled.find_element(By.CSS_SELECTOR, "action-link other-options-link")
    other_options_button.click()

    # Wait for the element to be present and then click it
    duo_push_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Duo Push')]"))
    )
    duo_push_button.click()


    # duo_security_key_wait.send_keys(Keys.RETURN)


    # Step 5: Handle "Stay signed in" prompt
    duo_stay_signed_in_button = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.ID, "trust-browser-button"))
    )

    # print(f"Found trust browser button! {duo_stay_signed_in_button.text}")
    duo_stay_signed_in_button.click()


    # Step 6: Handle "Stay signed in" prompt on microsoft
    microsoft_stay_signed_in_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "idBtn_Back"))
    )
    microsoft_stay_signed_in_button.click()


def looping_send(
        shadow_tree, 
        text_box, 
        long_text
    ):
    text_iterator = text_splitter(long_text, 7500)
    # print(f"Text: {text_itterator}")

    first_chunk = next(text_iterator)
    # print(f"Sending {first_chunk}")


    text_box.send_keys(first_chunk)
    time.sleep(10)
    
    text_box.send_keys(Keys.RETURN)

    for chunk in text_iterator:
        
        # print(f"Currently Working on this chunk: {chunk}")
        
        
        # Wait for cib-typing-indicator to appear within shadow_root_2
        WebDriverWait(shadow_tree["cib_serp"]["children"]["cib_action_bar"]["root"], 500).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'cib-typing-indicator[visible=""]'))
        )
        print("Typing indicator appeared")

        text_box.send_keys(chunk)

        

        # Wait for cib-typing-indicator to disappear within shadow_root_2
        WebDriverWait(shadow_tree["cib_serp"]["children"]["cib_action_bar"]["root"], 500).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, 'cib-typing-indicator[visible=""]'))
        )
        print("Typing indicator disappeared")

        time.sleep(1)

        write_responses(shadow_tree, -1)

        time.sleep(1)

        text_box.send_keys(Keys.RETURN)

    # Wait for the last response to be finished
    WebDriverWait(shadow_tree["cib_serp"]["children"]["cib_action_bar"]["root"], 500).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'cib-typing-indicator[visible=""]'))
    )

    print("Typing indicator appeared")

    WebDriverWait(shadow_tree["cib_serp"]["children"]["cib_action_bar"]["root"], 500).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, 'cib-typing-indicator[visible=""]'))
    )

    print("Typing indicator disappeared")
    time.sleep(10)
    # Final update of the output file
    write_responses(shadow_tree)

def write_responses(shadow_tree, response_number=None):
    chat_turns = shadow_tree["cib_serp"]["children"]["cib_conversation"]["root"].find_elements(By.CSS_SELECTOR, "cib-chat-turn")

    if (response_number == -1):
        if (len(chat_turns) >= 1):
            second_to_latest_conversation = chat_turns[-1]

            shadow_root_conversation = driver.execute_script('return arguments[0].shadowRoot', second_to_latest_conversation)

            shadow_host_cib_message_group = shadow_root_conversation.find_element(By.CSS_SELECTOR, "cib-message-group[source='bot']")
            shadow_root_cib_message_group = driver.execute_script('return arguments[0].shadowRoot', shadow_host_cib_message_group)

            copilot_response = shadow_root_cib_message_group.find_element(By.CSS_SELECTOR, "cib-message")
            response_text = copilot_response.get_attribute("aria-label")

            # print(response_text)
            write_to_file(response_text)
    if (response_number == None):
        # Delete whatever is in the file currently
        clear_file()
        for chat_turn in chat_turns:
            shadow_root_conversation = driver.execute_script('return arguments[0].shadowRoot', chat_turn)

            shadow_host_cib_message_group = shadow_root_conversation.find_element(By.CSS_SELECTOR, "cib-message-group[source='bot']")
            shadow_root_cib_message_group = driver.execute_script('return arguments[0].shadowRoot', shadow_host_cib_message_group)

            copilot_response = shadow_root_cib_message_group.find_element(By.CSS_SELECTOR, "cib-message")
            response_text = copilot_response.get_attribute("aria-label")

            # print(response_text)
            write_to_file(response_text)

def split_text_simple(text, chunk_size):
    """Splits the text into chunks of specified size and returns a list of chunks."""
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

def text_splitter(text, chunk_size):
    """Splits the text into chunks based on sentence boundaries and returns an iterator."""
    text = re.sub(r'\n', ' ', text)
    sentences = re.split(r'(?<=[.!?]) +', text)
    current_chunk = ""
    
    for sentence in sentences:
        if len(current_chunk) + len(sentence) + 1 <= chunk_size:
            current_chunk += sentence + " "
        else:
            if current_chunk:
                yield current_chunk.strip()
            if len(sentence) > chunk_size:
                words = sentence.split()
                current_sentence = ""
                for word in words:
                    if len(current_sentence) + len(word) + 1 <= chunk_size:
                        current_sentence += word + " "
                    else:
                        yield current_sentence.strip()
                        current_sentence = word + " "
                if current_sentence:
                    yield current_sentence.strip()
            else:
                current_chunk = sentence + " "
    
    if current_chunk:
        yield current_chunk.strip()

def read_file_contents(filename):
    """Reads the contents of a text file and returns it as a string."""
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()
    
# Function to write text to a file
# def write_to_file(text, filename="conversations.md", overwrite=False):
#     with open(filename, "a") as file:
#         file.write(text + "\n")



def write_to_file(text, filename="conversations.md", overwrite=False):
    mode = "w" if overwrite else "a"
    with open(filename, mode, encoding="utf-8") as file:
        file.write(text + "\n")

def clear_file(filename="conversations.md", backup=False):
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



long_text = read_file_contents("in.txt")
send_long_text(long_text)

# Backup the output file just made
clear_file(backup=True)

print("Program Finished! Check the history folder for the final output")
