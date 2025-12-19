from flask import Flask, url_for

app = Flask(__name__)

@app.route('/test')
def test():
    pass

with app.test_request_context():
    print(url_for('test', station_id=['A', 'B']))
