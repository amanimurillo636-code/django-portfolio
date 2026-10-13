from django.contrib import admin
from .models import Student

admin.site.register(Student)

class Portfolio(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    title =