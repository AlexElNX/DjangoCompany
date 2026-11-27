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


def contacts_us(request, _=None):
    return render(request, "contacts.html", {"country": "United States"})

def contacts_ca(request, _=None):
    return render(request, "contacts.html", {"country": "Canada"})

def contacts_au(request, _=None):
    return render(request, "contacts.html", {"country": "Australia"})


def error_404_view(request, exception):
    return render(request, '404.html')