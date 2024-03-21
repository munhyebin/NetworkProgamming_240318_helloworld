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
   2. urls
      1. _playground_/hello/_ -> _say_hello()_