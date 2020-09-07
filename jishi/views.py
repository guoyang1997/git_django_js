from django.shortcuts import render,HttpResponse

# Create your views here.

def add(request):
    a = 1
    b = 2
    return HttpResponse(a+b)


def dev2(request):
    return HttpResponse("OK")
