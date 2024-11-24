from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Welcome to Django Server</h1>")


# Create your views here.
