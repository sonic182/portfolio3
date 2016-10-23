from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.utils.translation import ugettext as _

from courses.models import Course
from courses.forms import StudentForm, MailListForm
# Create your views here.

def index(request):
    courses = Course.objects.filter(active=True)
    form = MailListForm()
    res = {
        'courses': courses,
        'title': _('Cursos'),
        'meta_description': _('meta_description_courses')
    }
    if request.method == 'POST':
        form = MailListForm(request.POST)
        if form.is_valid():
            obj = form.save()
            send_mail('Mail List Mogollon cursos', 'Nuevo inscrito en la lista de cursos: ' + obj.email, 'johanderson@mogollon.com.ve', ['johander1822@gmail.com'], fail_silently=False)
            return render(request, 'courses/index.html', {**res, **{'suscribed': True, 'form': form}})
    return render(request, 'courses/index.html', {**res, **{'form': form}})

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
        'form': student,
        'title': '{course}: {course_title}'.format(course=_('Course'), course_title=course.title),
        'meta_description': '{course}: {course_meta_description}'.format(course_meta_description=course.meta_description, course=_('Course'))
    })

def thanks(request):
    return render(request, 'courses/thanks.html')
