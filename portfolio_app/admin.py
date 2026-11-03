from django.contrib import admin
from django.db import models
from .models import Student, Portfolio

admin.site.register(Student)
admin.site.register(Portfolio)


