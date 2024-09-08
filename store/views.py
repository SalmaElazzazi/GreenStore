from django.shortcuts import render
from plants.models import Plant

# Create your views here.
def home(request):
    plants = Plant.objects.filter(is_available=True).order_by('-plant_date')[:6]
    context = {
        "title": "Home page",
        "plants": plants,
    }
    return render(request, 'store/home.html', context)
