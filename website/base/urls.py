from django.urls import path
from . import views


app_name = "base"

urlpatterns = [
    
    path('', views.home_view, name='home'),
    path('all-user', views.user_view, name='all-user'),
    path('add-post', views.add_post_view, name='add-post'),
    path('posts/<int:post_id>', views.post_detail_view, name='post'),

]