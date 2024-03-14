from django.http import HttpResponse
class ExampleMiddleware:

    def __init__(self, get_response) -> None:
        self.get_response = get_response
        print("**** By Class Based ****")
        print(" --> One Time Initialization ")

    def __call__(self,request, *args, **kwds):
        print("----- This is before view ------") # in here we can write something which we want to call before calling view 
        response = self.get_response(request)
        # print(request.META.get('HTTP_USER_AGENT'))
        print("------ This is after view ------") # in here we can write something which we want to call after calling view 
        return response
    
    def process_exception(self,request,exception):
        print("---- Exception middleware --------")
        msg = exception
        return HttpResponse(msg)