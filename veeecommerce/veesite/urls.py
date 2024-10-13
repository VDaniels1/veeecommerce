from django.urls import path
from .views import base, login_user, signup, product_list,product_detail,home,about,contact



urlpatterns =[
    path('', home),
    path('login/', login_user),
    path('signup/', signup),
     path('products/', product_list),
    path('products/<int:product_id>/', product_detail),
    path('about/',about),
    path('contact/',contact),
] 
