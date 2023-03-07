from .models import Order


def update_stock(products, quantities):
    for item in range(len(products)):
        product = products[item]
        quantidade = quantities[item]
        product_obj = Order.objects.get(id=product.id)
        if product_obj.stock < quantidade:
            raise ValueError(f'O produto {product_obj.name} está indisponível.')
        product_obj.stock -= quantidade
        product_obj.save()
