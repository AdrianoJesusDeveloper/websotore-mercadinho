from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def create_order(request):
    # Lógica para criar um pedido
    return JsonResponse({'message': 'Pedido criado com sucesso'})

def order_detail(request, pk):
    # Lógica para visualizar os detalhes do pedido
    return JsonResponse({'message': f'Detalhes do pedido {pk}'})

def order_list(request):
    # Lógica para listar todos os pedidos
    return JsonResponse({'message': 'Lista de pedidos'})
