from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if (postData['first_name'].isalpha()) == False:
            if len(postData['first_name']) < 3:
                errors['first_name'] = "First name can not be shorter than 3 characters"

        if (postData['last_name'].isalpha()) == False:
            if len(postData['last_name']) < 3:
                errors['last_name'] = "Last name can not be shorter than 3 characters"

        if len(postData['password']) < 8:
            errors['password'] = "Password is too short"

        if postData['password'] != postData['confirm']:
            errors['comfirm']= "Passwords doesn't match Confirm pw"


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    date = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
