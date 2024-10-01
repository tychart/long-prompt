from flask import Flask, request, render_template, jsonify
import subprocess

app = Flask(__name__)

def read_file_contents(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def run_separate_script(input_text):
    result = subprocess.run(['python', 'main.py', input_text], capture_output=True, text=True)
    return result.stdout

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    text = request.form['text']
    print(f"entered the submit function, this is the text: {text}")
    output = run_separate_script(text)
    return render_template('index.html', output=output)

@app.route('/get_output', methods=['GET'])
def get_output():
    return jsonify({'content': read_file_contents('out.md')})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
