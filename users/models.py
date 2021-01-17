from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'avatar7.png', upload_to = 'profile_pics')
    roll_no = models.CharField(default = 'None', max_length = 9)
    room_no = models.IntegerField(default = '0',)
    department = models.CharField(default = 'Update your department', max_length = 1000)
    year = models.CharField(default='Update your year', max_length=1000)
    gc_participation = models.CharField(default = 'None', max_length = 1000)
    interests_sports = models.CharField(max_length=100, default = '', blank=True)
    interests_cult = models.CharField(max_length=100, default = '', blank=True)
    interests_tech = models.CharField(max_length=100, default = '', blank=True)
    awards = models.CharField(default = 'None', max_length = 150)
    num_e_certificates = models.IntegerField(default = '0')
    e_certificate_1 = models.ImageField(default = 'default_2.jpg',upload_to = 'profile_pics')
    e_certificate_2 = models.ImageField(default = 'default_2.jpg',upload_to = 'profile_pics')
    e_certificate_3 = models.ImageField(default = 'default_2.jpg',upload_to = 'profile_pics')
    e_certificate_4 = models.ImageField(default = 'default_2.jpg',upload_to = 'profile_pics')
    e_certificate_5 = models.ImageField(default = 'default_2.jpg',upload_to = 'profile_pics')

    
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.interests_tech:
            self.interests_sports= eval(self.interests_sports)
            self.interests_cult= eval(self.interests_cult)
            self.interests_tech= eval(self.interests_tech)


 

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)