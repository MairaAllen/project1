from django.urls import path
from . import views
urlpatterns = [
    #path(route, view, name)
    #route - строка, которая содержит url, именно с ней маршрутизатор сопоставляет url с запроса
    #view - функция определенного маршрута(route), будет автоматически запущена, если какой-то из
    # route подошел с url-запроса
    #url_name - имя нашей ссылки, которую необходимо использовать при создании
    # ссылки вместо указывания полного пути

    #вместо (http://127.0.0.1:8000/landing/home/)


    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    #создаем url 'course/<int:pk>', где pk - уникальный идентификатор.
    #также важно, чтобы параметр функции назывался точно также, как и в urls.py

    path('course/<int:pk>', views.course, name='course'),
    path('check_leads/', views.check_leads, name='check_leads')
]


