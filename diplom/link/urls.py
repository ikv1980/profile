from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listlink.as_view(template_name='link/link.html'), name='link'),
    path('<str:short>/', views.GoToLink),
    # Удаление ссылки
    path('del_link/<link_id>/', views.delete_link),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

