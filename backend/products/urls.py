from django.urls import URLPattern, path

from . import views

urlpatterns = [
    path('', views.product_create_view), #/api/products/
    path('li/', views.product_list_create_view),
    path('<int:pk>/', views.product_detail_view),
    path('all/', views.product_list_view),
    path('alt/', views.product_alt_view),
    path('alt/<int:pk>/', views.product_alt_view),
    path('<int:pk>/update/', views.product_update_view),
    path('<int:pk>/destroy/', views.product_destroy_view),
    path('pm/', views.product_list_model_mixin),
    path('<int:pk>/pm/', views.product_list_model_mixin),
    path('pm/post/', views.product_list_model_mixin)

    
]