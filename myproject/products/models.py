from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.title

class Lawyer(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='lawyers/')  # فیلد تصویر

    def __str__(self):
        return self.name
    
class ImageTitle(models.Model):
    title = models.CharField(max_length=200)  # فیلد برای تیتر
    image = models.ImageField(upload_to='images/')  # فیلد برای عکس

    def __str__(self):
        return self.title
    
class BackgroundImage(models.Model):
    image = models.ImageField(upload_to='backgrounds/')

    def __str__(self):
        return f"Background Image {self.id}"