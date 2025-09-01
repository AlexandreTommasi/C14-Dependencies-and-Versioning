from flask import Flask, render_template, jsonify
from cachorro import get_dog_image_url

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dog')
def get_dog():
    try:
        url = get_dog_image_url()
        return jsonify({'url': url})
    except Exception as e:
        return jsonify({'url': None})

if __name__ == '__main__':
    app.run(debug=True)
