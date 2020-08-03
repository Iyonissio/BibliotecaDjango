from django.shortcuts import render
from .models import Aluno

## CBV class based views
# https://docs.djangoproject.com/en/3.0/ref/class-based-views/
from django.views.generic.detail import DetailView

# Create your views here.

# Returns the list of all books with all details
def home(request):
    aluno = Aluno.objects.all()
    context = {"aluno":aluno}
    return render(request, "index.html", context)
