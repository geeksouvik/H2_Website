from django.contrib import admin
from .models import Profile
# Register your models here.



class ProfileAdmin(admin.ModelAdmin):

    list_display = ('user','roll_no', 'room_no', 'gc_participation', 'interests_sports', 'interests_cult','interests_tech', 'awards')
    list_filter = ('gc_participation', 'interests_sports', 'interests_cult','interests_tech', 'awards')

    
admin.site.register(Profile, ProfileAdmin)