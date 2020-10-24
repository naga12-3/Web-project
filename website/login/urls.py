from django.urls import path

from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('login',views.login,name="login"),
    path('donation',views.donation,name="donation"),
    path('profile',views.profile,name="profile")
]