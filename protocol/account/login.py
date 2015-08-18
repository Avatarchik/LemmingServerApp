from ..lib import response_maker
from ..db import account

def actionHandler(request):
	facebookID = request.param['facebookID']

	user = account.getUser(facebookID)
	return response_maker.success(user.nickName)

