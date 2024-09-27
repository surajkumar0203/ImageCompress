from django.dispatch import receiver
import os
from django.db.models.signals import post_save
from myapp.models import ImageModel
from PIL import Image



@receiver(post_save,sender=ImageModel)
def create_thumnail(sender,instance,created,**kwargs):
   
    if created:
        # Define the sizes you want to generate
        sizes = {
            'thumnail_small': (100, 100),
            'thumnail_medium': (500, 500),
            'thumnail_large': (800, 800),
        }
        # create temporary folder 
        os.mkdir('thumnails')
        for fields_name,size in sizes.items():
            img=Image.open(instance.original_image.path)
            img.thumbnail(size,Image.Resampling.LANCZOS)
            thum_name,extention=os.path.split(instance.original_image.name)

            extention=extention.lower()
            thum_file=f'{thum_name}_{size[0]}X{size[1]}{extention}'
            thum_path=f"thumnails/{thum_file}"
            img.save(thum_path)

