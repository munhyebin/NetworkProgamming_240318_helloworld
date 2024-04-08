# helloidol

---

1. startproject helloidol
   1. python -m pip install django~=4.2
   2. django-admin startproject _helloidol_ .
   3. [python manage.py migrate]
   4. python manage.py runserver
2. startapp _playground_
   1. Terminal
      1. python manage.py startapp _playground_
   2. helloidol/settings.py
      1. 'playground', in INSTALLED_APPS
3. playground/
   - 정보 전달: urls -> views -> (models -> )templates
   - 코드 작성: (models -> )views -> templates -> urls
   1. views
      1. _say_hello()_
      2. _say_hello_html()_
      3. _say_bye_html()_
      4. -> templates에 context 전달
   2. urls
      1. _playground/hello/_ -> _say_hello()_
      2. _playground/hello_html/_ -> _say_hello_html()_
   3. templates/playground/
      1. hello.html
      2. bye.html
4. helloidol/
   1. urls, playground/urls
      1. _playground/_ -> _hello/_ -> _say_hello()_
      2. _playground/_ -> _hello_html/_ -> _say_hello_html()_
      3. _playground/_ -> _bye_html/_ -> _say_bye_html()_
---
5. startapp 세븐틴
   1. Terminal
      1. python manage.py startapp 세븐틴
      2. hellonovel/settings.py
         1. '세븐틴', in INSTALLED_APPS
6. 세븐틴/
   1. views
      1. ~~show_정한()~~
      2. ~~show_승관()~~
      3. -> templates에 context 전달
      4. 정보를 하나로 묶고, 거기에서 꺼내오자
      5. show_멤버()
      6. image link -> image file(static)
      7. show_멤버리스트()
   2. templates/세븐틴/
      1. ~~정한.html~~
         1. title: 세븐틴 - 정한
         2. h1: 세븐틴
         3. h2: 정한
         4. img: 정한 프로필 사진
            1. border-radius: 50%
      2. ~~승관.html~~
      3. 멤버.html
         1. group_name, name, img_src
         2. `{% load static %} <img src="{% static img_src %}">`
         3. ```
            {% extends 'base.html' %}
            {% block title %}{%endblock %}
            {% block content %}{% endblock %}
            ```
      4. 멤버리스트.html
         1. {% url '앱이름:path이름' %}
         2. {% url '앱이름:path이름' 변수=값 %}
         3. ```
            {% extends 'base.html' %}
            {% block title %}{%endblock %}
            {% block content %}{% endblock %}
            ```
   3. urls
      1. ~~세븐틴/ -> 정한/ -> show_정한()~~
      2. ~~세븐틴/ -> 승관/ -> show_승관()~~
      3. 세븐틴/ -> <멤버>/ -> show_멤버(멤버)
      4. 세븐틴/ -> 멤버리스트/ -> show_멤버리스트()
   4. static/세븐틴/images/
      1. 승관.jpeg, 원영.jpeg, 호시.jpeg
7. templates/
   1. base.html
      ```
      {% block title %}{% endblock %}
      {% block css %}{%endblock %}
      {% block content %}{% endblock %}
      ```
8. helloworld/
   1. in TEMPLATES in setting.py
      1. 'DIRS' : [BASE_DIR / 'templates'],