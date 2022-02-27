from django.http import HttpResponse

# Create your views here.
def content(request):
    print("return content")
    return HttpResponse("content page", 200)