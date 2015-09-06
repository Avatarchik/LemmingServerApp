import sys, traceback

from ..common import response_maker
from ..db import account

def actionHandler(request):
	userID = request.param['userID']
	userType = request.param['userType']
	nickName = request.param['nickName']

	account.makeUser(userID, userType, nickName)
	return response_maker.success()

