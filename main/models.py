import uuid
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    product_image = models.ImageField(upload_to='product_images/', null=True, blank=True)  # Field untuk gambar
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.price} - {self.description}"
