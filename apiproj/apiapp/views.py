from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
import random as r
from rest_framework.decorators import api_view



# Create your views here.
def homeview(request):
    return HttpResponse("yes you are here")

def send(request):
    send_mail(
        'HELLO this is an autogenerated mail',
        'this mail signifies that you have visited the specifies URL',
        'amart@mail.com',
        ['amartya25m@gmail.com'],
        fail_silently=False,

    )
    return HttpResponse("you have just recieved mail ")
    
def otpgen(request):
    i = r.randint(10000,100000)
    send_mail(
        'This is an otp mail',
        'the otp for your account Django test account is is:'+str(i),
        'amart@mail.com',
        ['amartyamishra2503@gmail.com'],
        fail_silently=False,
    )
    return HttpResponse('please check your mail for otp')

# def otpcheck(request,otp):
