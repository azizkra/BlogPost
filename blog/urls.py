from django.urls import path, include
from . import views
from rest_framework import routers

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
    )

#----API-----
r1 = routers.DefaultRouter()
r1.register('',views.Post_List)


urlpatterns = [
    path("", PostListView.as_view(), name="blog-home"),
    path('user/<str:username>',UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path("about/", views.about, name="blog-about"),
    path("data/", views.get_data, name="blog-data"),
    
    #----API----
    path('postJS/', include(r1.urls)),
]
