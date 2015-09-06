from django.db import models

# Create your models here.
class User(models.Model):
	userID = models.CharField(primary_key=True, max_length=200)
	userType = models.CharField(max_length=30)
	nickName = models.CharField(max_length=30)
	record = models.FloatField(db_index=True, default=0)
	createdTime = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.userID

