# from django.http import HttpResponse
from django.shortcuts import render

from .models import Course, Step
from django.shortcuts import get_object_or_404


def course_list(request):
    # output = ', '.join([course.title for course in courses])
    # return HttpResponse(output)

    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})

def step_detail(request, course_pk, step_pk):
    step = get_object_or_404(Step, course_id=course_pk, pk=step_pk)
    return render(request, 'steps/step_detail.html', {'step': step})
