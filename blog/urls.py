from django.urls import path
from blog import views

urlpatterns = [
    # cbw
    path('cbw/blogs/', views.BlogListCreateAPIView.as_view(), name='cbw-blogs'),
    # path('cbw/blogs/<int:pk>', views.BlogAPIView.as_view(), name='cbw-blogs-detail'),
    path('cbw/blogs/<int:pk>', views.BlogRetriveUpdateDeleteAPIView.as_view(), name='cbw-blogs-list-create')
]