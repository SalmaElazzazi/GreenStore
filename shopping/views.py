from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .cart import Cart
from .models import OrderItem
from .forms import CartAddProductForm , CheckoutForm
from django.contrib import messages
from plants.models import Plant


@require_POST
def cart_add(request, plant_id):
    cart = Cart(request)
    plant = get_object_or_404(Plant, id=plant_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(plant=plant, quantity=cd['quantity'], override_quantity=cd['override'])
        messages.success(request, f"{plant.name} has been successfully added to your cart.")
    return redirect('detail')

@require_POST
def cart_remove(request, plant_id):
    cart = Cart(request)
    plant = get_object_or_404(Plant, id=plant_id)
    cart.remove(plant)
    messages.success(request, f"{plant.name} has been removed  to your cart.")
    return redirect('cart')

@require_POST
def cart_update(request):
    cart = Cart(request)
    for key, value in request.POST.items():
        if key.startswith('quantity_'):
            plant_id = int(key.split('_')[1])
            try:
                plant = Plant.objects.get(id=plant_id)
                cart.add(plant=plant, quantity=int(value), override_quantity=True)
            except Plant.DoesNotExist:
                pass
    return redirect('cart')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'override': True})
        plant_id = item['plant'].id        
        plant = Plant.objects.get(id=plant_id)
        item['plant'] = plant
    context = {
        "cart": cart,
    }
    return render(request, 'shopping/cart_detail.html', context)

def checkout(request):
    cart = Cart(request)  
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user  
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    plant=item['plant'],
                    # price=item['price'],
                    quantity=item['quantity']
                )
            # Clear the cart
            cart.clear()
            messages.success(request, f"Your order (N° {order.id}) has been successfully processed. Thank you for your purchase!")
            return redirect('home')  # Redirect to a 'home' view, make sure this view exists
    else:
        form = CheckoutForm()
    
    context = {
        'cart': cart, 
        'form': form , 
        
        
    }
    return render(request, 'shopping/checkout.html', context)