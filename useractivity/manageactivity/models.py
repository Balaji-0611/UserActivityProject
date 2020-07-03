from django.db import models

# Create your models here.

# User Model
class User(models.Model):
    userId = models.CharField("ID", max_length = 150)
    realName = models.CharField("RealName", max_length = 150)
    timeZone = models.CharField("TimeZone", max_length = 150)

    def __str__(self):
        return self.userId

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    startTime = models.DateTimeField("StartTime")
    endTime = models.DateTimeField("EndTime")

    def __str__(self):
        return self.user.userId