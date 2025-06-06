from django.urls import path
from . import views 

urlpatterns = [

    path('', views.home, name=""),

    path('register', views.register,name="register"),

    path('my-login', views.my_login, name="my-login"),

    path('logout', views.logout, name="logout"),

    path('infopage', views.infopage, name="infopage"),

    path('account', views.account, name="account"),
]