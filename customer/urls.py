
from django.urls import path
from customer import views 
urlpatterns = [
    path('register', views.register, name='register'),
    path('login',views.login_redirect, name='login'),
    path('', views.index, name='index'),
    path('signout',views.signout, name='signout'),
    path('profile',views.profile, name='profile'),
    path('customer_update/<int:p_id>', views.update,name="customer_update"),
]
