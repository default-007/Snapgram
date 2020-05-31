from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('signup/', views.signup, name='signup'),
    url('', views.index, name='index'),
    url('profile/<username>/', views.profile, name='profile'),
    url('user_profile/<username>/', views.user_profile, name='user_profile'),
    url('post/<id>', views.post_comment, name='comment'),
]