from django.shortcuts import render , HttpResponse
from datetime import datetime
from home.models import Contact



# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()

        def __str__(self):
            return self.name


    return render(request,'contact.html')

def services(request):
    return render(request,'services.html')

def medicine(request):
    return render(request,'medicine.html')

def doctor(request):
    return render(request,'doctor.html')
def patient(request):
    return render(request,'patient.html')
def online(request):
    return render(request,'online.html')
def appointment(request):
    return render(request,'appointment.html')
def emergency(request):
    return render(request,'emergency.html')
def ambulance(request):
    return render(request,'ambulance.html')

