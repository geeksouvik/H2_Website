  
from django.contrib import admin
from .models import Profile
from import_export.admin import ImportExportModelAdmin


@admin.register(Profile )
class ViewAdmin(ImportExportModelAdmin):
    pass