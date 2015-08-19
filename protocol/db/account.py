from ...models import User

def getUser(facebook_id):
	try:
		return User.objects.get(facebookID = facebook_id)
	except User.DoesNotExist:
		return None

def makeUser(facebook_id, str_name):
	# FIXME: Check duplicated user.
	user = User(facebook_id, str_name)
	user.save()
