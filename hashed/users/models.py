from django.db import models

class user(models.Model):
    #usertoken
    username = models.CharField(max_length=50, default="")
    f_name = models.CharField(max_length=50, default="")
    l_name = models.CharField(max_length=50, default="")
    email = models.EmailField(max_length=30, default="")
    #hashed pass
    def __str__(self):
        return self.username
    
class credential(models.Model):
    #usertoken
    title = models.CharField(max_length=50, default="")
    website = models.URLField(max_length=100)
    #hashed pass
    #strength
    def __str__(self):
        return self.title