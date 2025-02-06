from itertools import chain
# from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import models
from django.shortcuts import get_object_or_404

from . import forms

 
def course_list(request):
    # output = ', '.join([course.title for course in courses])
    # return HttpResponse(output)

    courses = models.Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(models.Course, pk=pk)
    steps = sorted(chain(course.text_set.all(), course.quiz_set.all()), 
                   key=lambda step: step.order)
    return render(request, 'courses/course_detail.html', {
        'course': course, 
        'steps': steps
        })

def text_detail(request, course_pk, step_pk):
    step = get_object_or_404(models.Text, course_id=course_pk, pk=step_pk)
    return render(request, 'steps/step_detail.html', {'step': step})

def quiz_detail(request, course_pk, step_pk):
    step = get_object_or_404(models.Quiz, course_id=course_pk, pk=step_pk)
    return render(request, 'steps/step_detail.html', {'step': step})

def suggestion_view(request):
    form = forms.SuggestionForm()
    if request.method == 'POST':
        form = forms.SuggestionForm(request.POST)
        if form.is_valid():
            send_mail(
                'Suggestion from {}'.format(form.cleaned_data['name']), 
                form.cleaned_data['suggestion'],
                '{name} <{email}>'.format(**form.cleaned_data),
                ['mikebl2910@gmail.com']
            )
            messages.add_message(request, messages.SUCCESS, 'Thanks for your suggestion!')
            return HttpResponseRedirect(reverse('courses:suggestion'))

    return render(request, 'courses/suggestion_form.html', {'form': form})
