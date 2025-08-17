from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

def process_payment(request):
    # Lógica para processar o pagamento
    return JsonResponse({'message': 'Pagamento processado com sucesso'})

def payment_status(request, pk):
    # Lógica para verificar o status do pagamento
    return JsonResponse({'message': f'Status do pagamento {pk}'})

