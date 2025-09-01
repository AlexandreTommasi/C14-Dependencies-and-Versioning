from flask import Flask, render_template, jsonify
import subprocess
import sys
import os
from cachorro import get_dog_image_url

app = Flask(__name__)

@app.route('/')
def index():
    # Retorna status errado e conteúdo inesperado
    return 'Página não encontrada', 404

@app.route('/dog')
def get_dog():
    # Retorna formato inesperado e status errado
    return 'erro', 500

if __name__ == '__main__':
    app.run(debug=True)
