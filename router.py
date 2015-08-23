import sys, traceback

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from protocol.common import response_maker
from django.http import QueryDict

def checkLogin(request):
	if (request.param['sessionRequired'] == 'true'):
		return request.session['facebookID']
	else:
		return

@csrf_exempt
def route(request):
	splitedPaths = request.path.split('/')
	validSplitedPaths = splitedPaths[2 : len(splitedPaths)]
	protocol = splitedPaths[len(splitedPaths) - 1]
	protocolPath = '.'.join(validSplitedPaths);

	print('Requested value => ' + request.path)
	print('Requested path => ' + protocolPath)
	print('Requested Protocol => ' + protocol)
	print('Requested Param => ' + request.body)

	if request.method == 'GET':
		print('GET Request is not valid request')
		return HttpResponse(response_maker.error('get reqeust is not valid'))

	try:
		protocolModule  = __import__('protocol.' + protocolPath, globals(), locals(), [ protocol ], -1)
	except ImportError:	
		return HttpResponse(response_maker.error('Invalid protocol'))

	request.param = QueryDict(request.body)

	try:
		checkLogin(request)
	except KeyError:
		return HttpResponse(response_maker.error('You do not have permission'))

	try:
		return HttpResponse(protocolModule.actionHandler(request))
	except:
		error = traceback.format_exc()
		print(error)
		return HttpResponse(response_maker.error(error))

