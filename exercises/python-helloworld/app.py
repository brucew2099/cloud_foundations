from flask import Flask, json
import logging

app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info('Main request successfull')
    return "Hello World!"

@app.route('/status')
def health_status():
    response = app.response_class(
        response = json.dumps({'result': 'OK - Healthy'}),
        status = 200,
        mimetype ='application/json'
    )

    app.logger.info(response)
    return response

@app.route('/metrics')
def health_metrics():
    response = app.response_class(
        response=json.dumps({
            'status': 'success',
            'code': 0, 
            'data': {'UserCount': 140, 'UserCountActive': 23}
        }),
        status = 200,
        mimetype='application/json'
    )

    app.logger.info(response)
    return response

if __name__ == "__main__":

    logging.basicConfig(
        level=logging.DEBUG,
        filename='app.log',
        format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s',
    )

    app.run(host='0.0.0.0')
