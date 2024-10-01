Sure, I can help you turn your Python script into a simple web app. Here's a step-by-step guide to achieve this using Flask, a lightweight web framework for Python. We'll also set it up to run in a Docker container.

### Step 1: Create a Flask Web App

First, let's create a basic Flask web app that can accept text input and display the contents of `out.md`.

1. **Install Flask**:
   ```bash
   pip install flask
   ```

2. **Create the Flask App**:
   Create a file named `app.py` with the following content:
   ```python
   from flask import Flask, request, render_template
   import os

   app = Flask(__name__)

   def read_file_contents(filename):
       with open(filename, 'r', encoding='utf-8') as file:
           return file.read()

   @app.route('/', methods=['GET', 'POST'])
   def index():
       if request.method == 'POST':
           text = request.form['text']
           # Here you would call your Selenium script to process the text
           # For simplicity, we'll just write it to out.md
           with open('out.md', 'w', encoding='utf-8') as file:
               file.write(text)
           return read_file_contents('out.md')
       return render_template('index.html')

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)
   ```

3. **Create the HTML Template**:
   Create a folder named `templates` and inside it, create a file named `index.html` with the following content:
   ```html
   <!doctype html>
   <html lang="en">
     <head>
       <meta charset="utf-8">
       <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
       <title>Simple Web App</title>
     </head>
     <body>
       <div class="container">
         <h1>Submit Text</h1>
         <form method="post">
           <div class="form-group">
             <label for="text">Text</label>
             <textarea class="form-control" id="text" name="text" rows="3"></textarea>
           </div>
           <button type="submit" class="btn btn-primary">Submit</button>
         </form>
         {% if request.method == 'POST' %}
         <h2>Output</h2>
         <pre>{{ output }}</pre>
         {% endif %}
       </div>
     </body>
   </html>
   ```

### Step 2: Dockerize the Flask App

1. **Create a Dockerfile**:
   Create a file named `Dockerfile` with the following content:
   ```dockerfile
   FROM python:3.9-slim

   WORKDIR /app

   COPY requirements.txt requirements.txt
   RUN pip install -r requirements.txt

   COPY . .

   CMD ["python", "app.py"]
   ```

2. **Create a Requirements File**:
   Create a file named `requirements.txt` with the following content:
   ```plaintext
   flask
   python-dotenv
   selenium
   ```

3. **Build and Run the Docker Container**:
   ```bash
   docker build -t simple-webapp .
   docker run -p 5000:5000 simple-webapp
   ```

### Step 3: Integrate Your Selenium Script

You can integrate your Selenium script into the Flask app by calling it within the `index` route after receiving the text input. Make sure to handle the file operations appropriately.

This setup will allow you to submit text via the web interface, process it with your script, and display the output from `out.md`. Let me know if you need any further assistance!

Source: Conversation with Copilot, 9/30/2024
(1) github.com. https://github.com/faraadi/nord-ui/tree/31ca15dc863985fcb209da573e05ef14816f5319/site%2Fsrc%2Fassets%2Fdocuments%2Fgetting-started%2Fquick-start.md.
(2) github.com. https://github.com/MohtasimShariar/Playtube/tree/a2cafec8af6e9a8d60901426346974e5ec19d63e/index.php.
(3) github.com. https://github.com/maslakonetop/simontir/tree/ad61cdcfb3d79877958d7101f39b92848b3d26e7/testkode.php.
(4) github.com. https://github.com/timurmelnikov/tlaravel.loc/tree/aeadf6f5df0f7f05d959693abea46462dbd6468d/resources%2Fviews%2Fdefault%2Fcontact.blade.php.
(5) github.com. https://github.com/ShadowomaR/Facebook_Plus/tree/1a7069b0bad6b1ed84ba0fdab7c272a1b9141861/resources%2Fviews%2FForms%2Fcontact.blade.php.



My out.md file will be updated live, and I want my webapp to reflect that. Then when the script finishes, my output gets moved to a history folder. I want to have the file being viewed to switch to that new file



Got it! To achieve this, we can use Flask with JavaScript to periodically check for updates to `out.md` and display the latest content. When the script finishes and the file is moved to the history folder, the web app will switch to display the new file. Here's how you can do it:

### Step 1: Update the Flask App

1. **Modify `app.py`** to include an endpoint that returns the content of `out.md`:
   ```python
   from flask import Flask, request, render_template, jsonify
   import os
   import time

   app = Flask(__name__)

   def read_file_contents(filename):
       with open(filename, 'r', encoding='utf-8') as file:
           return file.read()

   @app.route('/', methods=['GET', 'POST'])
   def index():
       return render_template('index.html')

   @app.route('/get_output', methods=['GET'])
   def get_output():
       return jsonify({'content': read_file_contents('out.md')})

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)
   ```

2. **Update `index.html`** to include JavaScript for periodically fetching the latest content:
   ```html
   <!doctype html>
   <html lang="en">
     <head>
       <meta charset="utf-8">
       <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
       <title>Simple Web App</title>
       <script>
         function fetchOutput() {
           fetch('/get_output')
             .then(response => response.json())
             .then(data => {
               document.getElementById('output').innerText = data.content;
             });
         }

         setInterval(fetchOutput, 5000); // Fetch every 5 seconds
       </script>
     </head>
     <body>
       <div class="container">
         <h1>Submit Text</h1>
         <form method="post">
           <div class="form-group">
             <label for="text">Text</label>
             <textarea class="form-control" id="text" name="text" rows="3"></textarea>
           </div>
           <button type="submit" class="btn btn-primary">Submit</button>
         </form>
         <h2>Output</h2>
         <pre id="output"></pre>
       </div>
     </body>
   </html>
   ```

### Step 2: Handle File Movement and Switching

1. **Modify your script** to notify the web app when the file is moved:
   ```python
   import os
   import time
   from flask import Flask, request, render_template, jsonify

   app = Flask(__name__)

   def read_file_contents(filename):
       with open(filename, 'r', encoding='utf-8') as file:
           return file.read()

   @app.route('/', methods=['GET', 'POST'])
   def index():
       return render_template('index.html')

   @app.route('/get_output', methods=['GET'])
   def get_output():
       return jsonify({'content': read_file_contents('out.md')})

   @app.route('/switch_file', methods=['POST'])
   def switch_file():
       new_file = request.json.get('new_file')
       return jsonify({'content': read_file_contents(new_file)})

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)
   ```

2. **Update `index.html`** to handle file switching:
   ```html
   <!doctype html>
   <html lang="en">
     <head>
       <meta charset="utf-8">
       <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
       <title>Simple Web App</title>
       <script>
         function fetchOutput() {
           fetch('/get_output')
             .then(response => response.json())
             .then(data => {
               document.getElementById('output').innerText = data.content;
             });
         }

         function switchFile(newFile) {
           fetch('/switch_file', {
             method: 'POST',
             headers: {
               'Content-Type': 'application/json'
             },
             body: JSON.stringify({ new_file: newFile })
           })
           .then(response => response.json())
           .then(data => {
             document.getElementById('output').innerText = data.content;
           });
         }

         setInterval(fetchOutput, 5000); // Fetch every 5 seconds
       </script>
     </head>
     <body>
       <div class="container">
         <h1>Submit Text</h1>
         <form method="post">
           <div class="form-group">
             <label for="text">Text</label>
             <textarea class="form-control" id="text" name="text" rows="3"></textarea>
           </div>
           <button type="submit" class="btn btn-primary">Submit</button>
         </form>
         <h2>Output</h2>
         <pre id="output"></pre>
       </div>
     </body>
   </html>
   ```

3. **Modify your script** to notify the web app when the file is moved:
   ```python
   import os
   import time
   import requests

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

           # Notify the web app to switch to the new file
           requests.post('http://localhost:5000/switch_file', json={'new_file': backup_filename})

       # Clear the old file
       open(filename, "w").close()
   ```

This setup will allow your web app to reflect live updates to `out.md` and switch to the new file when the script finishes and moves the output to the history folder. Let me know if you need any further assistance!

Source: Conversation with Copilot, 9/30/2024
(1) github.com. https://github.com/MohtasimShariar/Playtube/tree/a2cafec8af6e9a8d60901426346974e5ec19d63e/index.php.
(2) github.com. https://github.com/maslakonetop/simontir/tree/ad61cdcfb3d79877958d7101f39b92848b3d26e7/testkode.php.
(3) github.com. https://github.com/timurmelnikov/tlaravel.loc/tree/aeadf6f5df0f7f05d959693abea46462dbd6468d/resources%2Fviews%2Fdefault%2Fcontact.blade.php.
(4) github.com. https://github.com/ShadowomaR/Facebook_Plus/tree/1a7069b0bad6b1ed84ba0fdab7c272a1b9141861/resources%2Fviews%2FForms%2Fcontact.blade.php.
