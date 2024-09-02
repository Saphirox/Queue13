import os

from pystalk import BeanstalkClient
from flask import Flask, request
import redis

TUBE_NAME = "MAIN_TUBE"

app = Flask(__name__)

@app.route("/beanstalk")
def beanstalk():
    client = BeanstalkClient('localhost', 11300)
    client.put_job_into(TUBE_NAME, request.args.get("message"))
    return "Success"

@app.route("/rdb")
def rdb():
    r = redis.Redis(host='localhost', port=6379)
    r.lpush(TUBE_NAME, str(request.args.get("message")))
    return "Success"

@app.route("/aof")
def aof():
    r = redis.Redis(host='localhost', port=6380)
    r.lpush(TUBE_NAME, str(request.args.get("message")))
    return "Success"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9091), debug=True)




