from django.http import HttpResponse

def home(request):
    print("I am home page")
    return HttpResponse("Home view page")