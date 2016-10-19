from __future__ import unicode_literals
import re
from django.db import models

class UserManager(models.Manager):
    def validate(self, email):
        print 'success'
        EMAIL_REGEX= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # if len(email)==0:
        #     print 'too short'
        #     return False

        if not re.match(EMAIL_REGEX, email):
            print 'False'
            return False

        else:
            print 'True'
            return True




class User(models.Model):
    email = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


    objects = UserManager()
