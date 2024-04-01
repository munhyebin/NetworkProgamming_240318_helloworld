from django.shortcuts import render

def show_정한(request):
    context = {
        'group_name' : '세븐틴',
        'name' : '정한',
        'img_src' : 'https://i.pinimg.com/550x/36/74/19/367419968ca254e73a973a39f36ca942.jpg',
    }
    return render(request, '세븐틴/멤버.html', context=context)
    # return render(request, '세븐틴/정한.html')

def show_승관(request):
    context = {
        'group_name' : '세븐틴',
        'name' : '승관',
        'img_src' : 'https://blog.kakaocdn.net/dn/Io8JL/btry8izWRw4/NIizXSzHiVDllrkkieyOuk/img.jpg',
    }
    return render(request, '세븐틴/멤버.html', context=context)
    # return render(request, '세븐틴/승관.html')
