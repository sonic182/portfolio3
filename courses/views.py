from django.shortcuts import render
from django.http import HttpResponse
from courses.models import Course
from courses.forms import StudentForm
# Create your views here.

def index(request):
    courses = Course.objects.filter(active=True)
    return render(request, 'courses/index.html', {
        'range': range(5),
        'courses': courses
    })

def show(request, id):
    student = StudentForm()
    if request.method == 'POST':
        student = StudentForm(request.POST)
        if student.is_valid():
            return HttpResponse('valid')
        else:
            return HttpResponse('no valid')
    else:
        course = Course.objects.get(id=id)
        return render(request, 'courses/show.html', {
            'course': course,
            'form': student
        })

def thanks(request, id):
    course = Course.objects.get(id=id)
    return render(request, 'courses/show.html', {
        'course': course
    })
