from rest_framework.response import Response
from functools import wraps

def authenticated_user(function) :
    @wraps(function)
    def wrapper_func(request, *args, **kwargs):
        
        if  'Authorization' in request.headers :
    
            return function(request, *args, **kwargs)

        else : 

            return Response({"message": "You are not authorized to use this API!"})

    return wrapper_func

        
     