from django.db import models



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



class AdminCouncil(models.Model):
    name = models.CharField(max_length=150)
    post = models.CharField(max_length=150)
    roomno = models.CharField(max_length=150,blank=True, default='')
    contactno = models.CharField(max_length=150,blank=True, default='')
    email = models.CharField(max_length=150)
    picture = models.ImageField(upload_to='images/')
    councillor = models.BooleanField(default=False)
    left = models.BooleanField(default=True)



    def __str__(self):
        return self.name

class WebCouncil(models.Model):
    name = models.CharField(max_length=150)
    post = models.CharField(max_length=150)
    roomno = models.CharField(max_length=150)
    contactno = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    picture = models.ImageField(upload_to='images/')
    councillor = models.BooleanField(default=False)
    left = models.BooleanField(default=True)



    def __str__(self):
        return self.name

class TechCouncil(models.Model):
    name = models.CharField(max_length=150)
    post = models.CharField(max_length=150)
    roomno = models.CharField(max_length=150)
    contactno = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    picture = models.ImageField(upload_to='images/')
    councillor = models.BooleanField(default=False)
    left = models.BooleanField(default=True)



    def __str__(self):
        return self.name

class MaintCouncil(models.Model):
    name = models.CharField(max_length=150)
    post = models.CharField(max_length=150)
    roomno = models.CharField(max_length=150)
    contactno = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    picture = models.ImageField(upload_to='images/')
    councillor = models.BooleanField(default=False)
    left = models.BooleanField(default=True)



    def __str__(self):
        return self.name

class CultCouncil(models.Model):
    name = models.CharField(max_length=150)
    post = models.CharField(max_length=150)
    roomno = models.CharField(max_length=150)
    contactno = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    picture = models.ImageField(upload_to='images/')
    councillor = models.BooleanField(default=False)
    left = models.BooleanField(default=True)



    def __str__(self):
        return self.name

class MessCouncil(models.Model):
    name = models.CharField(max_length=150)
    post = models.CharField(max_length=150)
    roomno = models.CharField(max_length=150)
    contactno = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    picture = models.ImageField(upload_to='images/')
    councillor = models.BooleanField(default=False)
    left = models.BooleanField(default=True)



    def __str__(self):
        return self.name

class SportsCouncil(models.Model):
    name = models.CharField(max_length=150)
    post = models.CharField(max_length=150)
    roomno = models.CharField(max_length=150)
    contactno = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    picture = models.ImageField(upload_to='images/')
    councillor = models.BooleanField(default=False)
    left = models.BooleanField(default=True)



    def __str__(self):
        return self.name

class EventsCouncil(models.Model):
    name = models.CharField(max_length=150)
    post = models.CharField(max_length=150)
    roomno = models.CharField(max_length=150)
    contactno = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    picture = models.ImageField(upload_to='images/')
    councillor = models.BooleanField(default=False)
    left = models.BooleanField(default=True)



    def __str__(self):
        return self.name



class AlumniTestimony(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    year = models.IntegerField()
    branch = models.CharField(max_length=150)
    testimony = models.TextField(max_length=5000)
    pic = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
