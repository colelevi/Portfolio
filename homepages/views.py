from django.shortcuts import render

# Create your views here.
def indexPageView(request):
    return render(request, 'index.html')

def aboutPageView(request):
    return render(request, 'homepages/about.html')

def contactPageView(request):
    return render(request, 'homepages/contact.html')

def tableauPageView(request):
    return render(request, 'misc/tableau.html')

