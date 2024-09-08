from django.shortcuts import render, get_object_or_404 , redirect
from .models import Plant, Category , Review
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import NewReviewForm

def plants(request):
    # Récupérer la catégorie et le tri sélectionnés via la requête GET
    category_id = request.GET.get('category')
    sorting = request.GET.get('order_by')
    categories = Category.objects.all()
    
    # Filtrer les plantes en fonction de la catégorie sélectionnée
    if category_id:
        plants = Plant.objects.filter(is_available=True, category_id=category_id)
    else:
        plants = Plant.objects.filter(is_available=True)
        
    # Appliquer le tri sélectionné
    if sorting == "latest":
        plants = plants.order_by('-plant_date')
    elif sorting == "lowtohigh":
        plants = plants.order_by('price')
    elif sorting == "hightolow":
        plants = plants.order_by('-price')
    
    paginator = Paginator(plants, 6) 
    page = request.GET.get('page')    
    try:
        plants = paginator.page(page)
    except PageNotAnInteger:
        plants = paginator.page(1)
    except EmptyPage:
        plants = paginator.page(paginator.num_pages)
    
    context = {
        'title': 'Plants',
        'plants': plants,
        'categories': categories,
        'orderby_list': ["rating", "latest", "lowtohigh", "hightolow"],
    }
    return render(request, 'plants/plants.html', context)

def plant_detail(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    reviews =  Review.objects.filter(plant=plant)[:3]
    if request.method == 'POST':
        review_form = NewReviewForm(data=request.POST) 
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.plant = plant 
            new_review.save()
            review_form = NewReviewForm()
    else:
        review_form = NewReviewForm() 
    plants =  Plant.objects.filter(is_available=True, category=plant.category)[:4]
    context = {
        'title': plant.name,
        'plant': plant,
        'review_form': review_form,
        'plants': plants,
        'reviews' : reviews ,
    }
    return render(request, 'plants/plant_detail.html', context)
