from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Cart, CartItem

# 🛒 Detalhes do carrinho
def cart_detail(request):
    cart = Cart.objects.first()  # Exemplo simples, idealmente vinculado ao usuário
    items = CartItem.objects.filter(cart=cart)
    data = {
        'cart_id': cart.id,
        'items': [
            {'product': item.product.name, 'quantity': item.quantity}
            for item in items
        ]
    }
    return JsonResponse(data)

# ➕ Adicionar item ao carrinho
@require_POST
def add_to_cart(request):
    # TODO: implementar lógica real
    return JsonResponse({'message': 'Item adicionado ao carrinho'})

# ➖ Remover item do carrinho
@require_POST
def remove_from_cart(request):
    # TODO: implementar lógica real
    return JsonResponse({'message': 'Item removido do carrinho'})

# 🧹 Limpar carrinho
@require_POST
def clear_cart(request):
    # TODO: implementar lógica real
    return JsonResponse({'message': 'Carrinho limpo'})

# 🔄 Atualizar quantidade de item
@require_POST
def update_cart_item(request):
    item_id = request.POST.get('item_id')
    quantity = request.POST.get('quantity')

    item = get_object_or_404(CartItem, id=item_id)
    item.quantity = quantity
    item.save()

    return JsonResponse({'message': 'Item atualizado com sucesso'})

# 🎟 Aplicar desconto
@require_POST
def apply_discount(request):
    discount_code = request.POST.get('discount_code')
    # TODO: lógica de validação de código
    return JsonResponse({'message': 'Desconto aplicado com sucesso', 'code': discount_code})

# 💾 Salvar item para depois
@require_POST
def save_for_later(request):
    item_id = request.POST.get('item_id')

    item = get_object_or_404(CartItem, id=item_id)
    item.save_for_later = True
    item.save()

    return JsonResponse({'message': 'Item salvo para depois'})

# 🔁 Mover item de volta para o carrinho
@require_POST
def move_to_cart(request):
    item_id = request.POST.get('item_id')

    item = get_object_or_404(CartItem, id=item_id)
    item.save_for_later = False
    item.save()

    return JsonResponse({'message': 'Item movido para o carrinho'})

# ✅ Finalizar compra
@require_POST
def checkout(request):
    # TODO: lógica de pagamento e finalização
    return JsonResponse({'message': 'Compra finalizada com sucesso'})
