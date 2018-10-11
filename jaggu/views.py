from django.shortcuts import render
from django.http import HttpResponse 
def home(request):
    print(request.user)
    template_name='jaggu/home.html'
    return render(request,template_name)
# Create your views here.
