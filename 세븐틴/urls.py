from django.urls import path

from 세븐틴 import views

app_name = '세븐틴'

urlpatterns = [
    path('정한/', views.show_정한, name='정한'),
    path('승관/', views.show_승관, name='승관'),
]