from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('menu', views.menu, name='menu'),
    path('register', views.register_page, name='register_page'),
    path('login', views.login_page, name='login_page'),
    path('logout', views.logout_user, name='logout_user')

]
