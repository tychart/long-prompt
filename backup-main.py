import re
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://copilot.microsoft.com")

# Vars
email = "tychart@byu.edu"
org_password = "PR5f1bhHepyO"

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


        web_elements = {}

        # Step 7: Ensure you are back on the original page
        # shadow_host_1_cib_serp = WebDriverWait(driver, 10).until(
        web_elements["cib_serp"]["host"] = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "cib-serp"))
        )
        print("Back To Copilot!")
        shadow_root_1_cib_serp = driver.execute_script('return arguments[0].shadowRoot', web_elements["cib_serp"]["host"])


        shadow_host_2_cib_action_bar = shadow_root_1_cib_serp.find_element(By.CSS_SELECTOR, "cib-action-bar")
        shadow_root_2_cib_action_bar = driver.execute_script('return arguments[0].shadowRoot', shadow_host_2_cib_action_bar)

        shadow_host_2_cib_conversation = shadow_root_1_cib_serp.find_element(By.CSS_SELECTOR, "cib-conversation")
        shadow_root_2_cib_conversation = driver.execute_script('return arguments[0].shadowRoot', shadow_host_2_cib_conversation)


        shadow_host_3_cib_text_input = shadow_root_2_cib_action_bar.find_element(By.CSS_SELECTOR, "cib-text-input")
        shadow_root_3_cib_text_input = driver.execute_script('return arguments[0].shadowRoot', shadow_host_3_cib_text_input)

        # shadow_host_3_cib_text_input = shadow_root_2_cib_conversation.find_element(By.CSS_SELECTOR, "cib-text-input")
        # shadow_root_3_cib_text_input = driver.execute_script('return arguments[0].shadowRoot', shadow_host_3_cib_text_input)


        text_box = shadow_root_3_cib_text_input.find_element(By.CSS_SELECTOR, "textarea")
        send_button = shadow_root_2_cib_action_bar.find_element(By.CSS_SELECTOR, "button[aria-label='Submit']")

        looping_send(
            shadow_root_2_cib_action_bar, 
            shadow_root_2_cib_conversation, 
            shadow_root_3_cib_text_input, 
            text_box, 
            send_button, 
            long_text
        )



        '''
        text_box.send_keys("Hey this is a test for copilot!")

        send_button.click()
        
        
        # Wait for cib-typing-indicator to appear within shadow_root_2
        typing_indicator = WebDriverWait(shadow_root_2, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'cib-typing-indicator[visible=""]'))
        )
        print("Typing indicator appeared")

        text_box.send_keys("Hey this is a seccondary test for copilot!")

        # Wait for cib-typing-indicator to disappear within shadow_root_2
        WebDriverWait(shadow_root_2, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, 'cib-typing-indicator[visible=""]'))
        )
        print("Typing indicator disappeared")

        time.sleep(3)

        send_button.click()
        '''
        time.sleep(100000000)



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
        shadow_root_2_cib_action_bar, 
        shadow_root_2_cib_conversation, 
        shadow_root_3_cib_text_input, 
        text_box, 
        send_button, 
        long_text
    ):
    text_iterator = text_splitter(long_text, 7500)
    # print(f"Text: {text_itterator}")

    first_chunk = next(text_iterator)
    print(f"Sending {first_chunk}")


    text_box.send_keys(first_chunk)
    time.sleep(10)
    
    text_box.send_keys(Keys.RETURN)

    for chunk in text_iterator:
        
        print(f"Currently Working on this chunk: {chunk}")
        
        
        # Wait for cib-typing-indicator to appear within shadow_root_2
        WebDriverWait(shadow_root_2_cib_action_bar, 500).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'cib-typing-indicator[visible=""]'))
        )
        print("Typing indicator appeared")

        text_box.send_keys(chunk)

        chat_turns = shadow_root_2_cib_conversation.find_elements(By.CSS_SELECTOR, "cib-chat-turn")

        if (len(chat_turns) > 1):
            second_to_latest_conversation = chat_turns[-2]

            shadow_root_conversation = driver.execute_script('return arguments[0].shadowRoot', second_to_latest_conversation)

            shadow_host_cib_message_group = shadow_root_conversation.find_element(By.CSS_SELECTOR, "cib-message-group[source='bot']")
            shadow_root_cib_message_group = driver.execute_script('return arguments[0].shadowRoot', shadow_host_cib_message_group)

            copilot_response = shadow_root_cib_message_group.find_element(By.CSS_SELECTOR, "cib-message")
            response_text = copilot_response.get_attribute("aria-label")

            print(response_text)
            write_to_file(response_text)


        # Wait for cib-typing-indicator to disappear within shadow_root_2
        WebDriverWait(shadow_root_2_cib_action_bar, 500).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, 'cib-typing-indicator[visible=""]'))
        )
        print("Typing indicator disappeared")

        time.sleep(1)

        text_box.send_keys(Keys.RETURN)

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
def write_to_file(text, filename="conversations.md"):
    with open(filename, "a") as file:
        file.write(text + "\n")


long_text = read_file_contents("in.txt")
send_long_text(long_text)

