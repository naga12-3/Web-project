from django.urls import path

from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('donation',views.donation,name="donation"),
    path('profile',views.profile,name="profile"),
    path('diet',views.diet,name="diet"),
    path('diet2',views.diet2,name="diet2"),
    path('home2',views.home2,name="home2")
]