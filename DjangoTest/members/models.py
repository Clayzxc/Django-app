from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"

class Profile(models.Model):
  user = models.OneToOneField(User, models.CASCADE)
  image = models.ImageField(default='no_avatar_icon.png', upload_to='profile_pics')

  def __str__(self):
    return f"{self.user.username} Profile"