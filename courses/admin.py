from django.contrib import admin
from . import models

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'start_date', 'created_at', 'updated_at')
    list_filter = ('title', 'active', 'start_date', 'created_at', 'updated_at')
    # list_filter = ('active', 'start_date')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at', 'updated_at')
    list_filter = ('name', 'email', 'phone', 'created_at', 'updated_at')
    pass

admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Student, StudentAdmin)
