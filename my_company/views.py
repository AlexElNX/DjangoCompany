from django.shortcuts import render

def home(request, _=None):
    return render(request, "home.html")

def news(request, _=None):
    return render(request, "news.html")

def management(request, _=None):
    return render(request, "management.html")

def about(request, _=None):
    return render(request, "about.html")

def contacts(request, _=None):
    return render(request, "contacts.html")
