from django.urls import path
from blog import views

urlpatterns = [
    path('blogs/', views.list_blogs, name='list-blogs'),
    path('blog/<int:pk>/detail', views.detail_blog, name='detail-blog'),
    path('blogs/search/', views.search_blogs, name='search-blogs'),
    path('blogs/create/', views.blogs_create, name='blogs-create'),
    path('blogs/update/<int:pk>', views.blogs_update, name='blogs-update'),
    path('blogs/delete/<int:pk>', views.blogs_delete, name='blogs-delete'),


    path('mobile_blogs/', views.list_mobile_blogs, name='list-mobile-blogs'),
    path('mobile_blogs/<int:pk>/detail', views.detail_mobile_blogs, name='detail-blog'),
    path('mobile_blogs/search/', views.search_mobile_blogs, name='search-blogs')
]