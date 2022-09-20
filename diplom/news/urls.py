from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowNewsView.as_view(), name='news'),
    path('<str:username>', views.UserAllNewsView.as_view(), name='user-news'),
    path('<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'),
    path('add/', views.CreateNewsView.as_view(), name='news-add'),
    path('<int:pk>/update', views.UpdateNewsView.as_view(), name='news-update'),
    path('<int:pk>/delete', views.DeleteNewsView.as_view(), name='news-delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)