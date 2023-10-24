from .models import Todo
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(request):
     all = Todo.objects.all()
     return render(request,'hello.html', {'todos':all})

