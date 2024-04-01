from django.shortcuts import render

group = {
    'members': [
        {
            'group_name': '세븐틴',
            'name': '정한',
            'img_src': 'https://i.pinimg.com/550x/36/74/19/367419968ca254e73a973a39f36ca942.jpg',
        },
        {
            'group_name': '세븐틴',
            'name': '승관',
            'img_src': 'https://blog.kakaocdn.net/dn/Io8JL/btry8izWRw4/NIizXSzHiVDllrkkieyOuk/img.jpg',
        },
        {
            'group_name': '세븐틴',
            'name': '호시',
            'img_src': 'https://image.bugsm.co.kr/artist/images/1000/802323/80232314.jpg',
        },
    ]
}

def show_정한(request):
    context = list(filter(lambda member : '정한' in member['name'], group['members']))[0]
    #context = group['members'][0]
    return render(request, '세븐틴/멤버.html', context=context)
    # return render(request, '세븐틴/정한.html')


def show_승관(request):
    context = list(filter(lambda member: '승관' in member['name'], group['members']))[0]
    # context = group['members'][1]
    return render(request, '세븐틴/멤버.html', context=context)
    # return render(request, '세븐틴/승관.html')

def show_멤버(request, 멤버):
    context = list(filter(lambda member: 멤버 in member['name'], group['members']))[0]
    return render(request, '세븐틴/멤버.html', context=context)