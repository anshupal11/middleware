''' 

# **** By Function Based ****

def my_middleware(get_response):
    print("**** By Function Based ****")
    print(" --> One Time Initialization ")  #it runs only onces when the project started.

    def my_midd_function(request):
        print("----- This is before view ------") # in here we can write something which we want to call before calling view 
        response = get_response(request) # it is responsible for calling view function
        print("------ This is after view ------") # in here we can write something which we want to call after calling view 
        return response
    return my_midd_function

'''

# **** By Class Based ****

from django.http import HttpResponse
class ExampleMiddleware:

    def __init__(self, get_response) -> None:
        self.get_response = get_response
        print("**** By Class Based ****")
        print(" --> One Time Initialization ")

    def __call__(self,request, *args, **kwds):
        print("----- This is before view ------") # in here we can write something which we want to call before calling view 
        response = self.get_response(request)
        print(request.META.get('HTTP_USER_AGENT'))
        print("------ This is after view ------") # in here we can write something which we want to call after calling view 
        return response
    
'''
    # this will call before view function and if they have HttpResponse then it will return this middleware response.
    def process_view(self,request, *args, **kwds):
        print('----- "Leave before view" -----')
        # return None          # if you don't want to return this response
        return HttpResponse("Leave before view") #  it is using because if you want any response before view
    
        
'''