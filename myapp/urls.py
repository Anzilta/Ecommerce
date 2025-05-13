
from django.urls import path
from . import views

urlpatterns =[
   path("signup",views.register,name='signup'),
   path('login',views.login_view,name="login"),
   path('',views.home_view,name="home"),
   path('home1/',views.home1_view,name="home1"),
   path('addproduct/',views.add_product,name="add_product"),
   path('adminhome/',views.admin_view,name="admin_home"),
   path('admindashboard/',views.dashboard_view,name="admin_dashboard"),
   path('editprofile/',views.edit_view,name="update_user"),
   path('profile/',views.profile_view,name="profile"),
   path('logout/', views.logout_view, name='logout'),
   path('delete/<str:email>/',views.delete_view,name="delete"),
      path('image/',views.image_view,name="image"),

]