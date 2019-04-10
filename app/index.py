from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    request_json = request.get_json()
    review_text = request.form.getlist('reviewText')
    if len(review_text):
        return review_text[0]
    else:
        return f'Hello World!'

