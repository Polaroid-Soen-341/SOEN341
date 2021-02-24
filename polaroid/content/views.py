from django.shortcuts import render
from django.http import HttpResponse

def retrieve_picture(request, uuid_i):
    return ""
    
def index(request, uuid_i):
    print(uuid_i)
    return HttpResponse("<h1>Hello World</h1>")
