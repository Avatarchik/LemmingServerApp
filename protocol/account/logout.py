from ..lib import response_maker
from ..db import account

def actionHandler(request):
	del request.session['facebookID']
	return response_maker.success()
