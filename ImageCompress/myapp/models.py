from django.db import models

class ImageModel(models.Model):
    original_image=models.ImageField(upload_to="Image/")
