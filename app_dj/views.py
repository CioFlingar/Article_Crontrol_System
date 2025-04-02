from django.http import HttpResponse

def home(reuest):
    return HttpResponse("Hello, World!")


