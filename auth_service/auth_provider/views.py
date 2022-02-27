from django.http import HttpResponse
import json 


def hello_world(request):
    print("return hello-world")
    return HttpResponse("hello_world", 200)

def login(request):
    print("return login")
    return HttpResponse("login_page", 200)

def registration(request):
    print("return registration")
    return HttpResponse("regitration_page", 200)

def token(request):
    print("return token")
    return HttpResponse(json.dumps({"active": False}), 200)