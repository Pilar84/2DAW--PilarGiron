from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=200)
    country= models.CharField(max_length=200)
    short_bio= models.TextField()
    website= models.URLField()
    
    def __str__(self):
        return self.name
class Venue(models.Model):
    name = models.CharField(max_length=200)
    address= models.CharField(max_length=200)
    description= models.TextField()
    max_capacity= models.IntegerField()
    
    def __str__(self):
        return self.name

class Edition(models.Model):
    year= models.IntegerField()
    theme= models.CharField(max_length=200)
    start_date= models.DateField()
    end_date= models.DateField()
    
    def __str__(self):
        return f"{self.year} - {self.theme}"

class Installation(models.Model):
    title= models.CharField(max_length=200)
    opening_date= models.DateField()
    short_description= models.TextField()
    materials= models.CharField(max_length=200)
    
    
    #relaciones
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='installations')
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='installations')
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE, related_name='installations')
    
    def __str__(self):
        return self.title