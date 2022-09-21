from django.contrib import admin
from .models import Education

# Define the admin class
class EducationAdmin(admin.ModelAdmin):
    list_display = ('name', 'company')

# Register the admin class with the associated model
admin.site.register(Education, EducationAdmin)