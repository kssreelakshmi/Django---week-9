from django.urls import path
from core import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('sign-in/', views.sign_in, name='sign-in'),
    path('sign-out/', views.sign_out, name='sign-out'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('user-home/', views.home, name='home'),



    path('admin-signin/', views.admin_signin, name='admin-signin'),
    path('admin-home/all-users', views.admin_home, name='admin-home'),
    path('admin-home/user-create/', views.user_create, name='user-create'),

    path('admin-home/user-delete/<int:id>', views.user_delete, name='user_delete'),
    path('user-control/<int:id>/', views.user_control, name='user_control'),
    path('user-update/<int:id>/', views.user_update, name='user_update'),
]
