from django.db import models

class Register(models.Model):

    Name = models.CharField(max_length=50)
    Mobile = models.CharField(max_length=50)


