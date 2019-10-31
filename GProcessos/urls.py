from django.contrib import admin
from django.urls import path, include
from processo.views import arquivos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('processo.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('userfiles/', arquivos)
]
