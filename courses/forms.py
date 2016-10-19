from django import forms
from courses.models import Student, MailList

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone']

class MailListForm(forms.ModelForm):
    class Meta:
        model = MailList
        fields = ['email']
