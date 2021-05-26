from django.db import models
from django.db.models.fields import DateField


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name


class regester(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password =models.IntegerField()



    def __str__(self):
        return self.name

class courses(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    body = models.CharField(max_length=50)

    def __str__(self):
        return self.title



class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    date= models.DateField(auto_now_add=True)
    archive= models.BooleanField(default=False)


    def __str__(self):
        return self.title