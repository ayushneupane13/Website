from django.shortcuts import render, HttpResponse
from Bolano.models import Contact
from datetime import date
from django.db.models.functions import Extract
from django.contrib import messages


# Create your views here.
def index(request):
    context={
        'variable':"hello"
    }
    messages.success(request, "this is a test message")
    return render(request,'index.html',context)
    #return HttpResponse('This is Homepage')

def about(request):
    #return HttpResponse('This is about page')
    return render(request,'about.html')

def service(request):
    #return HttpResponse('This is service page')
    return render(request,'service.html')

def contact(request):
    #return HttpResponse('This is contact page')
    if request.method == "POST":
        email= request.POST.get('email')
        contact= Contact(email=email, date=date.today())
        contact.save()
        messages.success(request, 'Your Email has been sent!')
    return render(request,'contact.html')

def admin(request):
    #return HttpResponse('This is admin  page')
    return render(request,'admin.site.urls')