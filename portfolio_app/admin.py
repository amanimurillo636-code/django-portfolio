from django.contrib import admin
from django.db import models
from .models import Student, Portfolio

admin.site.register(Student)
admin.site.register(Portfolio)

class Portfolio(models.Model):
    student = models.OneToOneField( Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    contact_email = models.EmailField()
    is_active = models.BooleanField(default=True)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.title
