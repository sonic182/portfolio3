from django.shortcuts import render
from courses.models import Course
# Create your views here.

def index(request):
    courses = Course.objects.filter()
    return render(request, 'courses/index.html', {
        'range': range(5),
        'courses': courses
    })

def show(request, id):
    course = Course.objects.get(id=id)
    return render(request, 'courses/show.html', {
        'course': course
    })
