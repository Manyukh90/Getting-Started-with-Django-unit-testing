from django.views import generic
from .models import Student

# Create your views here.

class StudentListView(generic.ListView):
    model = Student
    paginate_by = 10 # the number of students to return in each page
        

class StudentView(generic.DetailView):
    model = Student         