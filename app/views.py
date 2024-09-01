from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"index.html")
def profile(request):
    return render(request,"profile.html")
def password(request):
    return render(request,"password.html")
    
# Create your views here.
