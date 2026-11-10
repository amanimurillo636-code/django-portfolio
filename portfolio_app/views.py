from django.shortcuts import render
from .models import Portfolio

# Create your views here.
from django.http import HttpResponse

def index(request):
    # Retrieve active portfolios
    active_portfolios = Portfolio.objects.filter(
        is_active=True
    )

    return render(
        # HTTP request
        request,
        #Template Django is rendering
        'portfolio_app/index.html',
        #Context dictionary
        {'active_portfolios': active_portfolios}
    )

from django.views.generic import ListView
from .models import Student

# List = all
# path must be created and put in urls.py
class StudentListView(ListView):
    model = Student
    template_name = 'portfolio_app/student_list.html'
    context_object_name = 'students'

# must import for every View
from django.views.generic import DetailView
from .models import Student

    # Detail = specific
class StudentDetailView(DetailView):
    model = Student
    template_name = 'portfolio_app/student_detail.html'
    context_object_name = 'student'
