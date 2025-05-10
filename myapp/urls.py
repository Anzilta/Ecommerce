
from django.urls import path
from . import views

urlpatterns =[
   path("signup",views.register,name='signup'),
   path('',views.login_view,name="login"),
   path('home/',views.home_view,name="home")
]