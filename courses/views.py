from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from django.core.mail import send_mail
from django.utils.translation import ugettext as _

from courses.forms import MailListForm
from courses.forms import StudentForm
from courses.models import Course
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
            send_mail(
                'Mail List Mogollon cursos',
                'Nuevo inscrito en la lista de cursos: ' + obj.email,
                'johanderson@mogollon.com.ve',
                ['johander1822@gmail.com'],
                fail_silently=False)
            return render(
                request,
                'courses/index.html',
                {**res, **{'suscribed': True, 'form': form}})
    return render(request, 'courses/index.html', {**res, **{'form': form}})


def show(request, _id):
    student = StudentForm()
    if request.method == 'POST':
        student = StudentForm(request.POST)
        if student.is_valid():
            student_obj = student.save(commit=False)
            student_obj.course = get_object_or_404(Course, id=_id, active=True)
            student_obj.save()
            msg = 'Nuevo estudiante: <br>{name} <br>{email} <br>{phone}'
            msg = msg.format(
                name=student_obj.name,
                email=student_obj.email,
                phone=student_obj.phone)
            send_mail(
                'Nuevo Student Mogollon Cursos',
                msg,
                'johanderson@mogollon.com.ve',
                ['johander1822@gmail.com'],
                fail_silently=False)
            return redirect('courses_thanks')
    course = get_object_or_404(Course, id=_id, active=True)
    course.views += 1
    course.save()
    return render(request, 'courses/show.html', {
        'course': course,
        'form': student,
        'title': '{course}: {course_title}'.format(
            course=_('Course'), course_title=course.title),
        'meta_description': '{course}: {course_meta_description}'.format(
            course_meta_description=course.meta_description,
            course=_('Course'))
    })


def preview(request, _id):
    student = StudentForm()
    course = get_object_or_404(Course, id=_id)
    return render(request, 'courses/show.html', {
        'course': course,
        'form': student,
        'title': '{course}: {course_title}'.format(
            course=_('Course'),
            course_title=course.title),
        'meta_description': '{course}: {course_meta_description}'.format(
            course_meta_description=course.meta_description,
            course=_('Course'))
    })


def thanks(request):
    return render(request, 'courses/thanks.html')
