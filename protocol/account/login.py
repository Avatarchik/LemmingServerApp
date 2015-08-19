from ..lib import response_maker
from ..db import account

def actionHandler(request):
	facebookID = request.param['facebookID']

	user = account.getUser(facebookID)

	if (user == None):
		return response_maker.error('not existed user')
	else:
		request.session['facebookID'] = facebookID
		return response_maker.success(user.name)

