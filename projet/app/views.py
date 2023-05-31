from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def portfolio(request):
    return render(request, 'app/portfolio.html')

def contact(request):
    return render(request, 'app/contact.html')

def blog(request):
    return render(request, 'app/blog.html')
