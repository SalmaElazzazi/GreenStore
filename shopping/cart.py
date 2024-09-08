from decimal import Decimal
from django.conf import settings
from plants.models import Plant

class Cart:
    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, plant, quantity=1, override_quantity=False):

        
        plant_id = str(plant.id)
        if plant_id not in self.cart:
            self.cart[plant_id] = {'quantity': 0, 'price': str(plant.price)}
        if override_quantity:
            self.cart[plant_id]['quantity'] = quantity
        else:
            self.cart[plant_id]['quantity'] += quantity
        self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, plant):

        plant_id = str(plant.id)
        if plant_id in self.cart:
            del self.cart[plant_id]
            self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the plants from the database.
        """
        plant_ids = self.cart.keys()
        # get the plant objects and add them to the cart
        plants = Plant.objects.filter(id__in=plant_ids)

        for plant in plants:
            item = self.cart[str(plant.id)]
            item['plant'] = plant
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()