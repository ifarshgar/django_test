from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
  return render(request, "hello.html", {'name': 'Tania'})

def get_score(request):
  return HttpResponse('Your score is 0')