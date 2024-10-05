from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """ The view to checkout  """
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Psk03RraP5RdWyWcCpKeEUatqaJ6OCY7ok0XDXqn53KRnTSayXOJIkaHUBEOQ1e4nLCH2tMtbAZR4OY7qdCsvlp00fXgD66F0',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)