from django.shortcuts import render


def homepage(request):
    return render(request, template_name="home/index.html")

def about(request):
    return render(request, template_name="home/about.html")