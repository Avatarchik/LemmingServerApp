from ..common import response_maker
from ..db import account

def actionHandler(request):
	users = account.getRankUsers()

	userRecords = map(lambda user: {
		'nickName' : user.nickName,
		'record' : user.record,
		'userID' : user.userID
	}, users)

	for i in range(len(userRecords)):
		userRecords[i]['rank'] = i + 1;

	return response_maker.success({ 'userRecords' : userRecords })

