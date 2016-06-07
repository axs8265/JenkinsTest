#import ibm_db as db2
import json
import os
from flask import Flask, jsonify, make_response, request

import orderDayToVendor as odv

app = Flask(__name__)

@app.route('/posthello', methods = ['POST'])
def hello_world():
  return 'Hi There!!' 

@app.route('/<string:input_list>/orderdaytovendor', methods = ['GET'])
def order_day_to_vendor(input_list):
"""
Web Order to day
"""
	# Split the comma seperated string values into a list 
	input_list = input_list.split(',')
	# Convert the string list into int list
	input_list = [int(i) for i in input_list]
	return str(odv.calculate_order_day_to_vendor(input_list))

if __name__ == '__main__':
  app.debug = True
  PORT = int(os.environ.get('PORT'))
  app.run(host = '0.0.0.0', port = PORT)