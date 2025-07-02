from django.urls import path
from . import views as v

urlpatterns = [
	path('sign-up/', v.render_sign_up_page, name='sign-up-page'),
	path('sign-in/', v.render_sign_in_page, name='sign-in-page')
]