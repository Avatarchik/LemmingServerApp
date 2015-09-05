import json

def success(value = ''):
	return json.dumps({ 'status': 'ok', 'result': [value] })

def error(error):
	return json.dumps({ 'status': 'fail', 'errorResult': error })
