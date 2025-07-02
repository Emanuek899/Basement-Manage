from django.urls import path
from . import views

urlpatterns = [
    path('auth/register', views.new_user, name='new-user'),
    path('auth/login', views.validate_user, name='validated-user'),
    path('auth/logout', views.logout_user, name='log-out'),
    path('auth/delete', views.del_user, name='delete-user')
]