from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')
    roll_no = models.CharField(default = 'None', max_length = 9)
    room_no = models.IntegerField(default = '0',)
    gc_participation = models.CharField(default = 'None', max_length = 1000)
    interests = models.CharField(max_length=100, default = '', blank=True)
    awards = models.CharField(default = 'None', max_length = 150)
    e_certificates = models.ImageField(default = 'default_2.jpg', upload_to = 'profile_pics')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.interests:
            self.interests= eval(self.interests)
 

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)