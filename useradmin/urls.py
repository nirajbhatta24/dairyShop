from django.urls import path

from useradmin import views

urlpatterns = [

    path('adminDashboard', views.adminDashboard),
    path('crudProduct', views.crudProduct),
    path('customer_delete/<int:p_id>',views.customer_delete),
    path('deletebill/<int:d_id>',views.deletebill),
    path('billing',views.billing),
    path('adduser',views.adduser,name='adduser'),
    path('userinfo',views.userinfo,name='viewuser'),
    path('edituser/<int:p_id>',views.edituser),
    path('updateuser/<int:p_id>',views.updateuser),
    path('deleteuser/<int:p_id>',views.deleteuser),
]