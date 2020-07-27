from django.shortcuts import render
from django.http import HttpResponse, request


# Create your views here.
def main(request):
    return render(request,'Abubakar_django_app/main.html')

def dashboard(request):
    return render(request,'Abubakar_django_app/dashboard.html')

def customer(request):
    return render(request,'Abubakar_django_app/customer.html')