from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField(max_length=250, blank=True)
    image = models.ImageField(upload_to='categories/', blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Plant(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='plants/')
    image_description = models.ImageField(upload_to='plants/description',null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    plant_date = models.DateTimeField(default=timezone.now)
    plant_update = models.DateTimeField(auto_now=True)
    new = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='plants')

    def __str__(self):
        return self.name

class Review(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=150,default="salma")
    email = models.EmailField(max_length=254, null=True, blank=True)
    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('plant', 'user')
    
    
    class Meta:
        ordering = ['-created_at']  

    def __str__(self):
        return f'Review by {self.name} for {self.plant.name}'