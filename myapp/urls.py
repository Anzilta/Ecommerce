
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns =[
   path("signup",views.register,name='signup'),
   path('login',views.login_view,name="login"),
   path('',views.home_view,name="home"),
   path('home1/',views.home1_view,name="home1"),
   path('addproduct/',views.addproduct_view,name="add_product"),
   path('products/',views.product_view,name="products"),
    path('homeproducts/',views.homeproduct_view,name="homeproducts"),
   path('admindashboard/',views.dashboard_view,name="admin_dashboard"),
   path('editprofile/',views.edit_view,name="update_user"),
   path('profile/',views.profile_view,name="profile"),
   path('logout/', views.logout_view, name='logout'),
   path('delete_user/<str:email>/',views.delete_user,name="deleteuser"),
   path('delete_product/<int:product_id>/',views.delete_product,name="deleteproduct"),
   path('addtocart/<int:product_id>/',views.addtocart_view,name="addtocart"),
   path('updatecart/<int:item_id>/',views.updatecart,name="updatecart"),
   path('deletecartitem/<int:item_id>/',views.deletecartitem,name='deletecartitem'),
   path('cart/',views.cart_view,name="cart"),
   path('deliverd/<int:order_id>/', views.deliverd_view, name='deliverd'),
   path('orderplaced/',views.orderplaced,name='orderplaced'),
   path('success/',views.success_view,name='success'),
   path('order/',views.order_view,name='order'),
   path('history/',views.history_view,name="history")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)