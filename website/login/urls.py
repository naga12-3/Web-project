from django.urls import path

from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('donation',views.donation,name="donation"),
    path('profile',views.profile,name="profile"),
    path('diet',views.diet,name="diet"),
    path('pdiet',views.pdiet,name="pdiet"),
    path('diet2',views.diet2,name="diet2"),
    path('home2',views.home2,name="home2"),
    path('volunteer',views.volunteer,name="volunteer"),
    path('map',views.map,name="map"),
     path('maps',views.maps,name="maps"),
      path('thankyou',views.thankyou,name="thankyou"),
      path('money',views.money,name="money"),
      path('aboutus',views.aboutus,name="aboutus"),
     path('aboutus2',views.aboutus2,name="aboutus2"),
     path('knowmore1',views.knowmore1,name="knowmore1"),
     path('knowmore2',views.knowmore2,name="knowmore2"),
     path('knowmore3',views.knowmore3,name="knowmore3"),
     path('knowmore12',views.knowmore12,name="knowmore12"),
     path('knowmore22',views.knowmore22,name="knowmore22"),
     path('knowmore32',views.knowmore32,name="knowmore32")
    
      
]