from django.urls import path

from . import views

urlpatterns=[
    path('login',views.login,name="login"),
    path('donation',views.donation,name="donation")
]