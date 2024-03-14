from rest_framework import generics
from .models import Dados
from .serializer import DadosSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render

class DadosListCreate(generics.ListCreateAPIView):
    queryset = Dados.objects.all()
    serializer_class = DadosSerializer

class DadosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dados.objects.all()
    serializer_class = DadosSerializer

class UltimoDado(APIView):
    def get(self, request):
        try:
            ultimo_dado = Dados.objects.latest('id')
            return render(request, 'ultimo_dado.html', {'ultimo_dado': ultimo_dado})
        except Dados.DoesNotExist:
            return Response({"message": "Nenhum dado encontrado no banco de dados."}, status=404)
        
class HistoricoDados(APIView):
    def get(self, request):
        try:
            historico_dados = Dados.objects.all()
            return render(request, 'historico_dados.html', {'historico_dados': historico_dados})
        except Dados.DoesNotExist:
            return Response({"message": "Nenhum dado encontrado no banco de dados."}, status=404)


