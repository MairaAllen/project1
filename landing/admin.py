from django.contrib import admin
from .models import *
#(Course, Teacher) #или * (импортировать всё)

admin.site.register(Course)

admin.site.register(Teacher)

admin.site.register(Lead)
# Register your models here.


