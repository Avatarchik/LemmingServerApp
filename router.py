import sys, traceback

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from protocol.lib import response_maker
from django.http import QueryDict

@csrf_exempt
def route(request):
	splitedPaths = request.path.split('/')
	validSplitedPaths = splitedPaths[2 : len(splitedPaths)]
	protocol = splitedPaths[len(splitedPaths) - 1]
	protocolPath = '.'.join(validSplitedPaths);

	print('Requested value => ' + request.path)
	print('Requested path => ' + protocolPath)
	print('Requested Protocol => ' + protocol)

	if request.method == 'GET':
		print('GET Request is not valid request')
		return HttpResponse(response_maker.error('get reqeust is not valid'))

	try:
		protocolModule  = __import__('protocol.' + protocolPath, globals(), locals(), [ protocol ], -1)
	except ImportError:
		print('Invalid protocol error')
		traceback.print_exc(file=sys.stdout)
		return HttpResponse(response_maker.error('invalid protocol'))

	request.param = QueryDict(request.body)
	response = protocolModule.actionHandler(request)
	return HttpResponse(response)
