from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  # This will render the `index.html` from the templates directory.
