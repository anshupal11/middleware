# **** By Class Based ****

class FirstMiddleware:

    def __init__(self, get_response) -> None:
        self.get_response = get_response
        print(" ----> One Time First Middleware Initialization ")

    def __call__(self,request, *args, **kwds):
        print("------ This is First Middleware before view ------") # in here we can write something which we want to call before calling view 
        response = self.get_response(request)
        print("------ This is First Middleware after view ------") # in here we can write something which we want to call after calling view 
        return response

class SecondMiddleware:

    def __init__(self, get_response) -> None:
        self.get_response = get_response
        print(" ----> One Time Second Middleware Initialization ")

    def __call__(self,request, *args, **kwds):
        print("------ This is Second Middleware before view ------") # in here we can write something which we want to call before calling view 
        response = self.get_response(request)
        print("------ This is Second Middleware after view ------") # in here we can write something which we want to call after calling view 
        return response

class ThirdMiddleware:

    def __init__(self, get_response) -> None:
        self.get_response = get_response
        print(" ----> One Time Third Middleware Initialization ")

    def __call__(self,request, *args, **kwds):
        print("------ This is Third Middleware before view ------") # in here we can write something which we want to call before calling view 
        response = self.get_response(request)
        print("------ This is Third Middleware after view ------") # in here we can write something which we want to call after calling view 
        return response
    



# ->FirstMiddleware->SecondMiddleware->ThirdMiddleware 
# <-FirstMiddleware<-SecondMiddleware<-ThirdMiddleware

# O/P 
# ------ This is First Middleware before view ------
# ------ This is Second Middleware before view ------
# ------ This is Third Middleware before view ------
# I am home page
# ------ This is Third Middleware after view ------
# ------ This is Second Middleware after view ------
# ------ This is First Middleware after view ------