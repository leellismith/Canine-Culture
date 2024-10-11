from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from wishlist.models import Wishlist
from products.models import Product

# Add Item to wishlist
@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)

    if created:
        # Item was successfully added
        messages.success(request, f'{product.name} has been added to your wishlist!')
    else:
        # Item already in wishlist
        messages.info(request, f'{product.name} is already in your wishlist.')
    # Returns user to added they added item
    return redirect(request.META.get('HTTP_REFERER', 'products'))


# Remove Item from the wishlist
@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.filter(user=request.user, product=product).delete()
    return redirect('wishlist')


# View the wishlist
@login_required
def view_wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    context = {
        'wishlist_items': wishlist_items,
    }

    return render(request, 'wishlist/wishlist.html', context)