from django.urls import path
from api.views import DadosListCreate, DadosDetail, UltimoDado, HistoricoDados

urlpatterns = [
    path('dados/', DadosListCreate.as_view(), name='dados-list-create'),
    path('dados/<int:pk>/', DadosDetail.as_view(), name='dados-detail'),
    path('ultimo_dado/', UltimoDado.as_view(), name='ultimo_dado'),
    path('historico_dados/', HistoricoDados.as_view(), name='historico_dados'),
]
