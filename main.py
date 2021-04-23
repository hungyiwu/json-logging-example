from flask import Flask, current_app
from flask.logging import default_handler
import logging
from pythonjsonlogger.jsonlogger import JsonFormatter

fh = logging.FileHandler('/var/log/app.log')
fmt = JsonFormatter('%(asctime)s %(levelname)s %(module)s %(message)s')
fh.setFormatter(fmt)

app = Flask(__name__)
app.logger.removeHandler(default_handler)
app.logger.addHandler(fh)
app.logger.setLevel(logging.INFO)

@app.route('/')
def main():
    current_app.logger.info({'name': 'info'})
    current_app.logger.error({'name': 'error'})
    return 'hello hwu'

if __name__ == '__main__':
    app.run(debug=True)

