from django.shortcuts import render, redirect
from django.http import HttpResponse
from courses.models import Course
from courses.forms import StudentForm, MailListForm
# Create your views here.

def index(request):
    courses = Course.objects.filter(active=True)
    form = MailListForm()
    if request.method == 'POST':
        form = MailListForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courses/index.html', {
                'courses': courses,
                'suscribed': True,
                'form': form
            })
    return render(request, 'courses/index.html', {
        'courses': courses,
        'form': form
    })

def show(request, id):
    student = StudentForm()
    if request.method == 'POST':
        student = StudentForm(request.POST)
        if student.is_valid():
            student_obj = student.save(commit=False)
            student_obj.course = Course.objects.get(id=id)
            student_obj.save()
            return redirect('courses_thanks')
    course = Course.objects.get(id=id)
    return render(request, 'courses/show.html', {
        'course': course,
        'form': student
    })

def thanks(request):
    return render(request, 'courses/thanks.html')
