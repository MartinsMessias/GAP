from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
                  path('login/', views.login, name='login'),
                  path('', views.index, name='index'),
                  path('divisao/', views.divisao, name='divisao'),
                  path('editar_divisao/<str:id>', views.editar_divisao, name='editar_divisao'),
                  path('excluir_div/<str:id>', views.excluir_div, name='excluir_divisao'),
                  path('cadastrar_div/', views.cadastrar_div, name='cadastrar_div'),
                  path('tipo/', views.tipo, name='tipo'),
                  path('editar_tipo/<str:id>', views.editar_tipo, name='editar_tipo'),
                  path('excluir_tipo/<str:id>', views.excluir_tipo, name='excluir_tipo'),
                  path('cadastrar_tipo/', views.cadastrar_tipo, name='cadastrar_tipo'),
                  path('cadastrar/', views.cadastrar, name='cadastrar'),
                  path('editar/<str:id>', views.editar, name='editar'),
                  path('caixas/', views.caixas, name='caixas'),
                  path('excluir/<str:id>', views.excluir, name='excluir'),
                  path('accounts/', views.accounts, name='accounts')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
