from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('signup/', views.signup, name='signup'),
    url('account/', include('django.contrib.auth.url')),
    url('', views.index, name='index'),
    url('profile/<username>/', views.profile, name='profile'),
    url('user_profile/<username>/', views.user_profile, name='user_profile'),
    url('post/<id>', views.post_comment, name='comment'),
    url('post/<id>/like', PostLikeToggle.as_view(), name='liked'),
    url('api/post/<id>/like', PostLikeAPIToggle.as_view(), name='liked-api'),
    url('like', views.like_post, name='like_post'),
    url('search/', views.search_profile, name='search'),
    url('unfollow/<to_unfollow>', views.unfollow, name='unfollow'),
    url('follow/<to_follow>', views.follow, name='follow')
]