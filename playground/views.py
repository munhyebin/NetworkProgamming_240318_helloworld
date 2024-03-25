from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def say_hello(request):
    return HttpResponse("Hllo World")

def say_hello_html(request):
    return render(request, 'playground/hello.html', {'name' : '혜빈아', 'greeting': '안녀엉~'})

def say_bye_html(request):
    context = {
        'singer' : '부승관',
        'title' : '동그라미',
    }
    return render(request, 'playground/bye.html', context = context)