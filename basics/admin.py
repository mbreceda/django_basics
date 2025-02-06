from django.contrib import admin
from .models import Course, Text, Quiz

# Register your models here.
admin.site.register(Course)
admin.site.register(Text)
admin.site.register(Quiz)