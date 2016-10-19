from django.db import models
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from django.db.models.signals import post_delete
from django.dispatch import receiver

class Course(models.Model):
    picture = models.ImageField(upload_to='courses_pics')
    title = models.CharField(max_length=100)
    description = RichTextUploadingField()
    author = models.CharField(max_length=100, default='Johanderson')
    start_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

@receiver(post_delete, sender=Course)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.picture.delete(False)

class Student(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=140)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    birthdate = models.DateField(blank=True, null=True)
    course = models.ForeignKey(Course)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        if self.first_name:
            return self.first_name + ' ' + self.last_name
        return self.name

class MailList(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.email
