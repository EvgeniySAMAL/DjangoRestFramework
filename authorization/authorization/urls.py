"""authorization URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from users.views import *
from rest_framework import routers#создание роутера

class MyCustomRouter(routers.SimpleRouter): #создание класса роутера
    routers = [
        routers.Route(url=r'{prerix}$',      #читает список статей
                      mapping={'get':'list'},
                      name='{basename}-list',
                      detail=False,
                      initkwargs={'suffix':'List'}),
        routers.Route(url=r'{prefix}/{lookup}$', #читаетстатью по её индификатору
                      mapping={'get': 'retrieve'},
                      name='{basename}-detail',
                      detail=True,
                      initkwargs={'suffix': 'Detail'}),
    ]

# routers = routers.SimpleRouter() #создание роутера
# routers = routers.DefaultRouter() #создание роутера
routers = MyCustomRouter()
routers.register(r'user',UserViewSet,basename='user')#регистрация UserViewSet
print(routers.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include(routers.urls)), #http://127.0.0.1:8000/api/v1/user/   использование роутера

    # path('api/v1/userlist/',UserViewSet.as_view({'get':'list'})),
    # path('api/v1/userlist/<int:pk>/',UserViewSet.as_view({'put':'update'})),

    # path('api/v1/userlist',UserAPIList.as_view()),
    # path('api/v1/userlist/<int:pk>/',UserAPIUpdate.as_view()),
    # path('api/v1/userdetail/<int:pk>/',UserAPIDetailView.as_view()),
]
