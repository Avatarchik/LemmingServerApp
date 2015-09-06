from ..common import response_maker
from ..db import account

def actionHandler(request):
	userID = request.session['userID']

	record = request.param['record']
	
	account.updateRecord(userID, record)
	return response_maker.success()

