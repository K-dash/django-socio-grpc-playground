from django.db import models

# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length=70)

class Post(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
