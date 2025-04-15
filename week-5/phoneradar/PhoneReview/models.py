from django.db import models
from django.utils import timezone

# Create your models here.

class Brand(models.Model):
    """Brand model to store phone brand information."""
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    manufacturing_since = models.IntegerField(help_text="Year when manufacturing started")
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class PhoneModel(models.Model):
    """Phone model information."""
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='models')
    model_name = models.CharField(max_length=100)
    launch_date = models.DateField()
    platform = models.CharField(max_length=50, help_text="OS platform (e.g., Android, iOS)")
    os_version = models.CharField(max_length=50, blank=True)
    processor = models.CharField(max_length=100, blank=True)
    ram = models.CharField(max_length=50, blank=True)
    storage = models.CharField(max_length=100, blank=True)
    display = models.CharField(max_length=100, blank=True)
    camera = models.CharField(max_length=100, blank=True)
    battery = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    def __str__(self):
        return f"{self.brand.name} {self.model_name}"
    
    class Meta:
        ordering = ['-launch_date']

class Review(models.Model):
    """Review model for phone reviews."""
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_published = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    pros = models.TextField(blank=True)
    cons = models.TextField(blank=True)
    external_link = models.URLField(blank=True, help_text="Link to external review article")
    models = models.ManyToManyField(PhoneModel, related_name='reviews')
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date_published']
