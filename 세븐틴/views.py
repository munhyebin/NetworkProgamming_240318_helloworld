from django.shortcuts import render

def show_정한(request):
    return render(request, '세븐틴/정한.html')

def show_승관(request):
    return render(request, '세븐틴/승관.html')
