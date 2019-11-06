from django.db import models
from django.db.models.deletion import CASCADE
# Create your models here.


class Id(models.Model):
    name=models.CharField("name",max_length=25)
    branch=models.CharField("branch",max_length=100)
    book=models.CharField("book",max_length=25)

    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='image', null=True)
    Id=models.ForeignKey(to=Id, on_delete=CASCADE, null=True)   
    dec=models.TextField()


    def __str__(self):
        return self.title


class User(models.Model):
    username=models.CharField("User name",max_length=25)
    email=models.EmailField("User email")
    password= models.CharField("User password",max_length=15)
    date=models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.username 
