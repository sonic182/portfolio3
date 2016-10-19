from django.contrib import admin
from . import models

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'start_date', 'created_at', 'updated_at')
    list_filter = ('title', 'active', 'start_date', 'created_at', 'updated_at')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'course', 'created_at', 'updated_at')
    list_filter = ('name', 'email', 'phone', 'course__title', 'created_at', 'updated_at')

class MailListAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at', 'updated_at')
    list_filter = ('email', 'created_at', 'updated_at')

admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Student, StudentAdmin)
admin.site.register(models.MailList, MailListAdmin)
