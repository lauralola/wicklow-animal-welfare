from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.TAX_BACK_THRESHOLD:
        tax_back_delta = settings.TAX_BACK_THRESHOLD - total
    else:
        tax_back_delta = 0
    order_total = total
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'tax_back_delta': tax_back_delta,
        'order_total': order_total,
    }

    return context
