from django.shortcuts import render

# Create your views here.
def index(request):
    return render(render, 'views/index.html')

def contact(request):
    return render(render, 'views/contact.html')

def about(request):
    return render(render, 'views/about.html')


