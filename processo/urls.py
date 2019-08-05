from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('', views.index, name='index'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('editar/<str:id>', views.editar, name='editar'),
    path('listar/', views.listar, name='listar'),
    path('listar/exibir/<str:id>', views.exibir, name='exibir'),
    path('buscar/', views.buscar, name='buscar'),
    path('config/', views.config, name='config'),
    path('excluir/<str:id>', views.excluir, name='excluir'),
    path('accounts/', views.accounts, name='accounts')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)