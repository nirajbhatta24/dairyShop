from django.urls import path
from billpage import views 
urlpatterns = [
    path('buy/<int:p_id>',views.buy, name='buy'),
    path('bill_create',views.bill_create, name='bill_create'),
    path('yourorder',views.yourorder, name='yourorder'),
    path('productdelete/<int:p_id>',views.product_delete, name='productdelete'),
    path('productedit/<int:p_id>',views.product_edit, name='productedit'),
    path('productupdate/<int:p_id>',views.product_update, name='productupdate'),

]