from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

#User Model: This includes fields such as username, email, 
#password (hashed), and any additional user information you may require.
class Signup(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Signin(models.Model):
    sno = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.email

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 

#Token Model: If you're implementing a system where users need tokens to cast their votes
#(to ensure one-person-one-vote), you might need a Token model to manage the issuance and validation of tokens.
