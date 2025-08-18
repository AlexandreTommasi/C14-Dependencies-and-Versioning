from flask import Flask, render_template, jsonify
import subprocess
import sys
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dog')
def get_dog():
    script_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'cachorro.py')
    result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
    output = result.stdout.strip()
    return jsonify({'url': 'main-branch-url'})

if __name__ == '__main__':
    app.run(debug=True)
