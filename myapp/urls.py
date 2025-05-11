
from django.urls import path
from . import views

urlpatterns =[
   path("signup",views.register,name='signup'),
   path('',views.login_view,name="login"),
   path('home/',views.home_view,name="home"),
   path('addproduct/',views.add_product,name="add_product"),
   path('adminhome/',views.admin_view,name="admin_home"),
   path('editprofile/',views.edit_view,name="update_user"),
   path('logout/', views.logout_view, name='logout'),
]