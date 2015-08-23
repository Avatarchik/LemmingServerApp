import sys, traceback

from ..common import response_maker
from ..db import account

def actionHandler(request):
	facebookID = request.param['facebookID']
	name = request.param['name']

	account.makeUser(facebookID, name)
	return response_maker.success()

