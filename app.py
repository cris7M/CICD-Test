from calendar import timegm
from datetime import datetime
import time
from flask import Flask, request, jsonify
app = Flask(__name__)

app.debug = True


def convert_to_time_ms(timestamp):
    return 1000 * timegm(datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ').timetuple())


@app.route('/')
def health_check():
    return 'This datasource is healthy.'


@app.route('/search', methods=['POST'])
def search():
    return jsonify(['my_series'])


@app.route('/query', methods=['POST'])
def query():
    req = request.get_json()
    print(req)
    data = [
        {
            "target": req['targets'][0]['target'],
            "datapoints": [
                [time.time()*4, convert_to_time_ms(req['range']['from'])],
                [time.time()*3, convert_to_time_ms(req['range']['to'])]
            ]
        }
    ]
    return jsonify(data)




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')