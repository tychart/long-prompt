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