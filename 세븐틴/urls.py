from django.urls import path

from 세븐틴 import views

app_name = '세븐틴'

urlpatterns = [
    path('멤버리스트/', views.show_멤버리스트, name='멤버리스트'),
    path('<멤버>/', views.show_멤버, name='멤버'),
    # path('정한/', views.show_정한, name='정한'),
    # path('승관/', views.show_승관, name='승관'),
]