from django.shortcuts import render


def homepage(request):
    return render(request, template_name="home/index.html")

def error_404(request, exception):
    return  render(request, template_name="errors/error_404.html")