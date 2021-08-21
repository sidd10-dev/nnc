from django.urls import path
from . import views

app_name = "nnc"

urlpatterns = [
    path('',views.home,name = 'home'),
    path('products/<slug:slug>/',views.productpage,name = 'product'),
    path('allproducts/',views.allproductpage, name = 'allproduct'),
    path('cart/',views.cart,name = 'cart'),
    path('addtocart/<int:pk>',views.addtocart,name = 'addtocart'),
    path('addtocartt/<int:pk>/<int:quantity>',views.addtocartt,name='addtocartt'),
    path('increase/<int:pk>',views.increaseqty,name = 'increase'),
    path('decrease/<int:pk>',views.decreaseqty,name = 'decrease'),
    path('remove/<int:pk>',views.remove,name = 'remove'),
    path('checkout/',views.checkout,name = 'checkout'),
    path('orders/',views.orders,name = 'orders'),
    path('order/<int:pk>',views.order_detail,name = 'orderdetail'),
    path('delivery/',views.delivery_page,name='delivery'),
    path('delivery/<int:pk>',views.delivery_detail,name='deliverydetail'),
    path('setdelivered/<int:pk>',views.set_delivered,name='setdelivered')
]