from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


@admin.register(Updates,Legend_Category,Legends,Council_Category,Council,AlumniTestimony,Post,Testimony )
class ViewAdmin(ImportExportModelAdmin):
    pass

