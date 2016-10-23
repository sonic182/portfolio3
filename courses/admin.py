from django.contrib import admin
from . import models

@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'start_date', 'views', 'created_at', 'updated_at')
    list_filter = ('title', 'active', 'start_date', 'created_at', 'updated_at')
    actions = ['active', 'deactive']

    def active(self, request, queryset):
        queryset.update(active=True)

    def deactive(self, request, queryset):
        queryset.update(active=False)


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'course', 'created_at', 'updated_at')
    list_filter = ('name', 'email', 'phone', 'course__title', 'created_at', 'updated_at')


@admin.register(models.MailList)
class MailListAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at', 'updated_at')
    list_filter = ('email', 'created_at', 'updated_at')
