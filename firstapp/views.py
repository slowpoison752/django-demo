from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    content={'some_dynamic_content':' SOME RANDOM DYNAMIC CONTENT FROM BACKEND'}
    return render(request,'firstapp/index.html', context=content)

# Create your views here.
