from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Category(models.Model):
    # Remember then to filer "Category.objects.filter(parent=None)"
    parent = models.ForeignKey('self', related_name='sub_categories', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=20, null=False)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=202)
    details = RichTextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    date_posted = models.DateField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    available = models.BooleanField(default=False, null=True, blank=True)
    cover = models.URLField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=False)
    surname = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=200, null=False)


    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class CartList(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   item = models.ManyToManyField(Product)
   def __str__(self):
       return f"{self.user}'s CartList"