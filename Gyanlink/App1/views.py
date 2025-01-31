from django.shortcuts import render, HttpResponse, redirect
from .models import student_info
# Create your views here.

def home(request):
    ab=student_info.objects.all()
    return render(request, 'index.html',{'show':ab})

def stusave(request):
    Id = request.POST['id']
    name = request.POST['name']
    email = request.POST['email']
    contactno = request.POST['contactno']

    ab = student_info(id=Id, name=name, email=email, contactno=contactno)
    ab.save()
    return redirect('home')