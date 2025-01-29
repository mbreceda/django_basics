from django.urls import path
from .views import course_list, course_detail, step_detail

app_name="courses"

urlpatterns = [
    path('course/', course_list, name='list'),
    path('course/<int:pk>/', course_detail, name='detail'),
    path('course/<int:course_pk>/step/<int:step_pk>/', step_detail, name='step')
]
