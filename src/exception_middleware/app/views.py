from django.http import HttpResponse

def home(request):
    print("I am home page")
    return HttpResponse("Home view page")

def excp(request):
    print("I am excp page")
    a = 10/0
    return HttpResponse("excp view page")