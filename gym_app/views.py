from django.shortcuts import render

# Create your views here.
def index_page(request):
    context = {}
    return render(request, 'index.html', context)
def portfolio(request):
    context = {}
    return render(request, 'portfolio-details.html', context)
def service(request):
    context = {}
    return render(request, 'service-details.html', context)
def starter_page(request):
    context = {}
    return render(request, 'starter-page.html', context)