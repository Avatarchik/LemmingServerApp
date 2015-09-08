from ...models import User

def getUser(user_id):
	try:
		return User.objects.get(userID = user_id)
	except User.DoesNotExist:
		return None

def makeUser(user_id, user_type, str_nickName):
	# FIXME: Check duplicated user.
	user = User(userID = user_id, userType = user_type, nickName = str_nickName)
	user.save()

def updateRecord(user_id, record):
	user = User.objects.get(userID = user_id)
	user.record = record
	user.save()

def getRankUsers():
	limitOfUsers = 50;
	rankUsers = User.objects.all().order_by('-record')[:limitOfUsers]
	return rankUsers

