from ..common import response_maker
from ..db import account

def actionHandler(request):
	userID = request.param['userID']

	user = account.getUser(userID)

	if (user == None):
		return response_maker.error('invalidUser')
	else:
		request.session['userID'] = userID
		return response_maker.success({
			nickName : user.nickName,
			record : user.record
			})

