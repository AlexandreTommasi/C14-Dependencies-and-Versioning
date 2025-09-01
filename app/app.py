from flask import Flask, render_template, jsonify
import subprocess
import sys
import os
from cachorro import get_dog_image_url

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dog')
def get_dog():
    try:
        img_url = get_dog_image_url()
        return jsonify({'url': img_url})
    except Exception as e:
        return jsonify({'url': None}), 200

if __name__ == '__main__':
    app.run(debug=True)
