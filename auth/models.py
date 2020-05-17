from django.db import models

class Author(models.Model):

    email = models.EmailField()
    username = models.CharField(max_length=20, default=None)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    
    account_linkedin = models.URLField()

