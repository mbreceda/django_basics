from django.urls import path
from . import views

app_name="courses"

urlpatterns = [
    path('', views.course_list, name='home'),
    path('course/', views.course_list, name='list'),
    path('course/<int:pk>/', views.course_detail, name='detail'),
    path('course/<int:course_pk>/text/<int:step_pk>/', views.text_detail, name='text'),
    path('course/<int:course_pk>/quiz/<int:step_pk>/', views.quiz_detail, name='quiz'),
    path('suggestion/', views.suggestion_view, name='suggestion'),
]
