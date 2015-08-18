from ...models import User

def getUser(facebook_id):
	try:
		return User.objects.get(facebookID = facebook_id)
	except User.DoesNotExist:
		return None

