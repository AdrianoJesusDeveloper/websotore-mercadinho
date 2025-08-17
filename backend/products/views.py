from django.http import JsonResponse
from .models import Product

def product_list(request):
    products = Product.objects.all()
    data = [
        {
            'id': p.id,
            'name': p.name,
            'price': float(p.price),
            'category': p.category.name,
            'created_at': p.created_at,
            'updated_at': p.updated_at
        }
        for p in products
    ]
    return JsonResponse({'products': data})

def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {
            'id': product.id,
            'name': product.name,
            'price': float(product.price),
            'category': product.category.name,
            'description': product.description,
            'created_at': product.created_at,
            'updated_at': product.updated_at
        }
        return JsonResponse({'product': data})
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Produto não encontrado'}, status=404)
