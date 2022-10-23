from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_sup>', views.delete, name='delete'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
