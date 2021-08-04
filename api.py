import sys
import os
from flask import Flask, jsonify
from dao import get_all_employees

port = os.environ['PORT']
app =   Flask(__name__)

@app.route("/", methods=["GET"])
def default():
  return jsonify({"message": "api is running"})


@app.route("/employees", methods=["GET"])
def index():
  employees = get_all_employees()
  return jsonify(employees)



if __name__ == "__main__":
  
  app.run(host="localhost", port=port, debug=True)