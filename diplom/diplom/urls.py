from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # Базовые страницы сайта
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('education/', views.education, name='education'),
    path('project/', views.project, name='project'),
    # Подключение дополнительных моделей Django
    path('users/', include('users.urls')),  # Модуль коротких ссылок
    path('link/', include('link.urls')),    # Модуль пользователей
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

