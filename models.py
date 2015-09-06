from django.db import models

# Create your models here.
class User(models.Model):
	userID = models.CharField(primary_key=True, max_length=200)
	userType = models.CharField(max_length=30)
	nickName = models.CharField(max_length=30)
	createdTime = models.DateTimeField(auto_now_add=True)

	def __init__(self, userID, userType, nickName)
		self.userID = userID
		self.userType = userType
		self.nickName = nickName

	def __str__(self):
		return self.userID

class Ranking(models.Model):
	user = models.ForeignKey(User, primary_key=True, unique=True)
	record = models.IntegerField(db_index=True, default=0)

	def __str__(self):
		return self.user
