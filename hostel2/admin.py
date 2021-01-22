from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


@admin.register(Updates,Legend_Category,Legends,Council,AlumniTestimony,Post )
class ViewAdmin(ImportExportModelAdmin):
    pass

@admin.register(Council_Category)
class ViewAdmin(ImportExportModelAdmin):
    pass