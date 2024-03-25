# helloworld

---

1. startproject helloworld
    1. python -m pip install django~=4.2
    2. django-admin startproject _helloworld_ .
    3. [python manage.py migrate]
    4. python manage.py runserver
2. startapp _playground_
   1. Terminal
      1. pythonmanage.py startapp _playground_
   2. helloworld/setting.py
      1. 'playground', in INSTALLED_APPS
3. playground/
   - 정보전달 : urls -> views -> (models -> )templates
   - 코드 작성 : (models ->) views -> templates -> urls
   1. views
      1. _say_hell()_
      2. _say_hello_html()_
      3. _say_bye_html()_
      4. -> templates에 context 전달
   2. urls
      1. _playground/hello/_ -> _say_hello()_
      2. _playground/hello_html_ -> _say_hello_html()_
   3. templates/playground/
      1. hello.html
      2. bye.html
4. helloworld/
   1. urls, playground/urls
      1. _playground/_ -> _hello/_ -> _say_hello()_
      2. _playground/_ -> _hello_html/_ -> _say_hello_html()_
      3. _playground/_ -> _bye_html/_ -> _say_bye_html()_