from ..common import response_maker
from ..db import account

def actionHandler(request):
	del request.session['userID']
	return response_maker.success()
