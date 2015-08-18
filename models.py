from django.db import models

# Create your models here.
class User(models.Model):
	facebookID = models.CharField(max_length=200)

class Ranking(models.Model):
	user = models.ForeignKey(User)
	record = models.IntegerField(db_index=True, default=0)
