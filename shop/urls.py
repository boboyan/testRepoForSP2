from django.urls import path, re_path, include
from . import views
from . import views
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.product_list, name='product_list'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus/', views.contactus, name='contactus'),
    path('signup/', views.signup, name='signup'),



    #######do not cross this line#####

    path('<slug:category_slug>/', views.product_list, 
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
]