from courses.models import MailList
from courses.models import Student
from django import forms


class StudentForm(forms.ModelForm):
    class Meta(object):
        model = Student
        fields = ['name', 'email', 'phone']


class MailListForm(forms.ModelForm):
    class Meta(object):
        model = MailList
        fields = ['email']
