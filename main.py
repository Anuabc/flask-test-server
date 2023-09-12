from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api')
def results():
    return jsonify({
        'name': 'test',
        'count': 1
    })

app.run()
