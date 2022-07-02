from django.urls import path

from . import views

app_name = 'auth'

urlpatterns = [
    path('login/', views.client_signin_view, name='signin'),
    path('signup/', views.client_signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),

]