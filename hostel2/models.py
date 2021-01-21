from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Updates(models.Model):
    name = models.CharField(max_length=150,primary_key=True,default = 'No New Update')
    def __str__(self):
        return self.name

class Legend_Category(models.Model):
    name = models.CharField(max_length=150,primary_key=True)
    id = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Legends(models.Model):
    type = models.ForeignKey(Legend_Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    year = models.IntegerField()

    def __str__(self):
        return self.name

class Council_Category(models.Model):
    category = models.CharField(max_length=150,primary_key=True)

    def __str__(self):
        return self.category


class Council(models.Model):
    category = models.ForeignKey(Council_Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    post = models.CharField(max_length=150)
    roomno = models.CharField(max_length=150,blank=True, default='')
    contactno = models.CharField(max_length=150,blank=True, default='')
    email = models.CharField(max_length=150)
    picture = models.ImageField(upload_to='images/')
    councillor = models.BooleanField(default=False)
    left = models.BooleanField(default=True)
    manifestoExists = models.BooleanField(default=False)
    socialmedia = models.CharField(max_length=150,default='#')
    manifesto = models.FileField(upload_to='manifesto/',blank=True,null=True )

    def __str__(self):
        return self.name

class AlumniTestimony(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    year = models.IntegerField()
    branch = models.CharField(max_length=150)
    testimony = models.TextField(max_length=5000)
    pic = models.ImageField(default = 'default.jpg', upload_to = 'testimonial/')

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

